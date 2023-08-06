from pathlib import Path

import voluptuous as vo

schema = vo.Schema(
    vo.All(
        {
            vo.Required("version"): vo.In([1.2]),
            vo.Optional("output"): vo.Coerce(Path),
            vo.Required("command"): str,
            vo.Optional("use_dask", default=False): bool,
        },
    )
)
