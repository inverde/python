# Define global variables
GLOBALS = {}
c_OFF = False
c_ON = True

# Create progam flags
GLOBALS['debug'] = c_OFF
GLOBALS['testing'] = c_OFF
GLOBALS['version'] = '1.0.0'

def  set_testing_mode(mode: bool =  c_ON) -> None:
    """Set the testing mode flag."""
    GLOBALS['testing'] = mode

def is_testing_mode() -> bool:
    """Check if the program is in testing mode."""
    return GLOBALS['testing']

def set_debug_mode(mode: bool = c_ON) -> None:
    """Set the debug mode flag."""
    GLOBALS['debug'] = mode

def is_debug_mode() -> bool:
    """Check if the program is in debug mode."""
    return GLOBALS['debug']

def get_version() -> str:
    """Get the current version of the program."""
    return GLOBALS['version']

def set_version(version: str = '1.0.0') -> None:
    """Set the current version of the program."""
    GLOBALS['version'] = version
