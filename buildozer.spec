[app]
# 应用标题
title = AutoClickApp
# 应用包名
package.name = autoclickapp
# 应用包域名
package.domain = com.example
# 主 Python 代码所在目录
source.dir = .
# 要包含的源文件扩展名
source.include_exts = py,png,jpg,kv,atlas
# 应用版本
version = 0.1
# 应用所需依赖
requirements = python3,kivy,uiautomator2

# 应用支持的屏幕方向
orientation = portrait

# 安卓平台设置
[app:android]
# 是否全屏显示
fullscreen = 0
# 应用所需权限
permissions = INTERNET,READ_EXTERNAL_STORAGE,WRITE_EXTERNAL_STORAGE,ACCESS_NOTIFICATION_POLICY,FOREGROUND_SERVICE,ACCESSIBILITY_SERVICE
# 目标 Android API 版本
api = 33
# 最低支持的 Android API 版本
minapi = 21
# Android SDK 版本
sdk = 33
# Android NDK 版本
ndk = 25.1.8937393
# 构建的 Android 架构
arch = armeabi-v7a

[buildozer]
# 日志级别
log_level = 2
# 是否在以 root 权限运行时发出警告
warn_on_root = 1