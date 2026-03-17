[app]
title = MyCamera
package.name = cameraapp
package.domain = org.test
source.dir = .
source.include_exts = py,png,jpg,kv,atlas
version = 0.1
requirements = python3,kivy
android.permissions = CAMERA, INTERNET
android.archs = arm64-v8a, armeabi-v7a
[buildozer]
log_level = 2
