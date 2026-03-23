import os
import platform

print("==================================")
print("    MINI SYSTEM PROFILER v1.0     ")
print("==================================")

system_os = platform.system()
os_version = platform.release()
print("Operating System: " + system_os + " " + os_version)

hostname = platform.node()
print("Hostname: " + hostname)

try:
    current_user = os.getlogin()
except OSError:
    current_user = os.environ.get('USERNAME') or os.environ.get('USER') or "Unknown"

print("Current User: " + current_user)

print("==================================")
print("        PROFILING COMPLETE        ")
print("==================================")