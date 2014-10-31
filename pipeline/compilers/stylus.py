from __future__ import unicode_literals

from pipeline.conf import settings
from pipeline.compilers import SubProcessCompiler


class StylusCompiler(SubProcessCompiler):
    output_extension = 'css'

    def match_file(self, filename):
        return filename.endswith('.styl')

    def compile_file(self, infile, outfile, outdated=False, force=False, cwd=None):
        command = "%s %s %s" % (
            settings.PIPELINE_STYLUS_BINARY,
            settings.PIPELINE_STYLUS_ARGUMENTS,
            infile
        )
        return self.execute_command(command, cwd=cwd)
