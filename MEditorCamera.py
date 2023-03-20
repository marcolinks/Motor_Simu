from ursina import *
from ursina.shaders import *

class MEditorCamera(Entity):
    def __init__(self, **kwargs):
        camera.editor_position = camera.position
        super().__init__(name='editor_camera', eternal=False)

        self.gizmo = Entity(parent=self, model='sphere', color=color.orange, scale=.025, add_to_scene_entities=False, enabled=False)

        self.rotation_speed = 200
        self.pan_speed = Vec2(5, 5)
        self.move_speed = 10
        self.zoom_speed = 1.25
        self.zoom_smoothing = 8
        self.rotate_around_entity = False

        self.smoothing_helper = Entity(add_to_scene_entities=True)
        self.rotation_smoothing = 0

        for key, value in kwargs.items():
            setattr(self, key, value)

        self.start_position = (0,0,0)
        self.perspective_fov = camera.fov
        self.orthographic_fov = camera.fov
        self.on_destroy = self.on_disable
        self.hotkeys = {'toggle_orthographic':'shift+p', 'focus':'f', 'reset_center':'shift+f'}


    def on_enable(self):
        camera.org_parent = camera.parent
        camera.org_position = camera.position
        camera.org_rotation = camera.rotation
        camera.parent = self
        camera.position = camera.editor_position
        camera.rotation = (0,0,0)
        self.target_z = camera.z


    def on_disable(self):
        #camera.editor_position = camera.position
        camera.parent = camera.org_parent
        camera.position = camera.org_position
        camera.rotation = camera.org_rotation


    def on_destroy(self):
        destroy(self.smoothing_helper)


    def input(self, key):
        combined_key = ''.join(e+'+' for e in ('control', 'shift', 'alt') if held_keys[e] and not e == key) + key

        if combined_key == self.hotkeys['toggle_orthographic']:
            if not camera.orthographic:
                self.orthographic_fov = camera.fov
                camera.fov = self.perspective_fov
            else:
                self.perspective_fov = camera.fov
                camera.fov = self.orthographic_fov

            camera.orthographic = not camera.orthographic


        elif combined_key == self.hotkeys['reset_center']:
            self.animate_position(self.start_position, duration=.1, curve=curve.linear)

        elif combined_key == self.hotkeys['focus'] and mouse.world_point:
            self.animate_position(mouse.world_point, duration=.1, curve=curve.linear)


        elif key == 'scroll up':
            if not camera.orthographic:
                target_position = self.world_position
                #if mouse.hovered_entity and not mouse.hovered_entity.has_ancestor(camera):
                #     target_position = mouse.world_point

                self.world_position = lerp(self.world_position, target_position, self.zoom_speed * time.dt * 10)
                self.target_z += self.zoom_speed * (abs(self.target_z)*.1)
            else:
                camera.fov -= self.zoom_speed * (abs(self.target_z)*.1)

        elif key == 'scroll down':
            if not camera.orthographic:
                # camera.world_position += camera.back * self.zoom_speed * 100 * time.dt * (abs(camera.z)*.1)
                self.target_z -= self.zoom_speed * (abs(camera.z)*.1)
            else:
                camera.fov += self.zoom_speed * (abs(camera.z)*.1)
        
        elif key == 'right mouse down':
            if self.rotate_around_entity:
                org_pos = camera.world_position
                self.world_position = self.get_pos
                camera.world_position = org_pos
                



    def update(self):
        if mouse.right:
            self.smoothing_helper.rotation_x -= mouse.velocity[1] * self.rotation_speed
            self.smoothing_helper.rotation_y += mouse.velocity[0] * self.rotation_speed
            
            self.direction = Vec3(
                self.forward * (held_keys['w'] - held_keys['s'])
                + self.right * (held_keys['d'] - held_keys['a'])
                + self.up    * (held_keys['e'] - held_keys['q'])
                ).normalized()
            
            self.position += self.direction * (self.move_speed + (self.move_speed * held_keys['shift']) - (self.move_speed*.9 * held_keys['alt'])) * time.dt
            
            
            if self.target_z < 0:
                self.target_z += held_keys['w'] * (self.move_speed + (self.move_speed * held_keys['shift']) - (self.move_speed*.9 * held_keys['alt'])) * time.dt
            else:
                self.position += camera.forward * held_keys['w'] * (self.move_speed + (self.move_speed * held_keys['shift']) - (self.move_speed*.9 * held_keys['alt'])) * time.dt

            self.target_z -= held_keys['s'] * (self.move_speed + (self.move_speed * held_keys['shift']) - (self.move_speed*.9 * held_keys['alt'])) * time.dt
            
        if mouse.left:
            if not camera.orthographic:
                zoom_compensation = -self.target_z * .1
            else:
                zoom_compensation = camera.orthographic * camera.fov * .2

            self.position -= camera.right * mouse.velocity[0] * self.pan_speed[0] * zoom_compensation
            self.position -= camera.up * mouse.velocity[1] * self.pan_speed[1] * zoom_compensation

        camera.z = lerp(camera.z, self.target_z, time.dt*self.zoom_smoothing)

        if self.rotation_smoothing == 0:
            self.rotation = self.smoothing_helper.rotation
        else:
            self.quat = slerp(self.quat, self.smoothing_helper.quat, time.dt*self.rotation_smoothing)
            camera.world_rotation_z = 0


    def __setattr__(self, name, value):
        super().__setattr__(name, value)
        if hasattr(self, 'smoothing_helper') and name in ('rotation', 'rotation_x', 'rotation_y', 'rotation_z'):
            setattr(self.smoothing_helper, name, value)
