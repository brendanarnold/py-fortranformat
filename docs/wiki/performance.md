Using v1.2.0 calculate `FortranRecordWriter('5F10.4')` 50000 times takes around 2.854s.

Short-cutting the `_compose_float_string()` function with an early return reduces this to 0.778s meaning there is up to 4x savings in that function alone.
