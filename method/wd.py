from gdo.base.GDT import GDT
from gdo.base.Method import Method
from gdo.core.GDT_Bool import GDT_Bool
from gdo.core.GDT_Float import GDT_Float
from gdo.core.GDT_String import GDT_String


class wd(Method):

    def __init__(self):
        super().__init__()

    def gdo_parameters(self) -> [GDT]:
        return [
            GDT_Bool('all').not_null().initial('0'),
            GDT_Bool('warn').not_null().initial('0'),
            GDT_String('pattern').not_null().initial('*'),
            GDT_Float('threshold').not_null().initial('3.141569'),
        ]
