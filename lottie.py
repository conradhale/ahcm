#!/usr/bin/env python3
from zipfile import ZipFile, ZIP_DEFLATED
from pathlib import Path
import json

def create_dotlottie(name: str):
    src = Path(f'lottie/{name}')

    with ZipFile(f'public/{name}.lottie', 'w', ZIP_DEFLATED) as zip:
        for root, _, files in src.walk():
            for file in files:
                path = root.joinpath(file)
                if path.suffix == '.json':
                    with open(path, 'r') as fp:
                        zip.writestr(
                            path.relative_to(src).as_posix(),
                            json.dumps(json.load(fp))
                        )
                else:
                    zip.write(
                        path,
                        path.relative_to(src),
                    )

create_dotlottie('logo')
