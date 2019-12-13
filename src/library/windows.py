import sys


def enable_hidpi_support():
    # Try to tell Windows we're HiDPI aware, to disable scaling
    if sys.platform == 'win32':
        try:
            import ctypes
            PROCESS_SYSTEM_DPI_AWARE = 1
            ctypes.OleDLL('shcore').SetProcessDpiAwareness(PROCESS_SYSTEM_DPI_AWARE)
        except (AttributeError, OSError):
            pass

# TODO have a function to determine DPI so text elements can be scaled appropriately
