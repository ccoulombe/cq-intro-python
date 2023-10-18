#!/bin/env python3

import json
import os
import argparse

def to_empty(cell):
    code_cell = cell['cell_type'] == 'code'
    to_empty = 'empty' in cell['metadata'].get('tags', [])
    return code_cell and to_empty

def main(args):
    for file in args.FILES:
        content = json.load(file)

        for cell in filter(to_empty, content['cells']):
                cell['source'] = []

        if args.inplace:
            outname = file.name
        elif args.outputdir:
            outname = os.path.join(args.outputdir, os.path.basename(file.name))
        else: # fallback to avoid erasing files in case we are in the directory
            outname = f"{os.path.basename(file.name)}.new"

        with open(outname, 'w', encoding="UTF-8") as out:
            json.dump(content, out, indent=1, ensure_ascii=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument("FILES", nargs='+', type=argparse.FileType('r'))

    output_group = parser.add_argument_group('output')
    parser.add_mutually_exclusive_group()._group_actions.extend([
        parser.add_argument("-o", "--outputdir", help='Write stripped files to output directory'),
        parser.add_argument("-i", "--inplace", action='store_true', help='Work in-place, modifying current file')
    ])

    main(parser.parse_args())
