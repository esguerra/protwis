from build.management.commands.base_build import Command as BaseBuild

from structure.models import Structure
from structure.functions import StructureBuildCheck


class Command(BaseBuild):

    def add_arguments(self, parser):
        super(Command, self).add_arguments(parser=parser)

    def handle(self, *args, **options):
        sbc = StructureBuildCheck()
        sbc.check_structures()
        structs = Structure.objects.all()
        for s in structs:
            sbc.check_segment_ends(s)
        print("Missing segments: ", len(sbc.missing_seg))
        for i in sbc.missing_seg:
            print("Error: Missing segment {} {} has no residue objects. Should have {} to {}".format(i[0],i[1],i[2],i[3]))
        print("Start errors: ", len(sbc.start_error))
        for i in sbc.start_error:
            print("Error: {} {} starts at {} instead of annotated {}".format(i[0],i[1],i[2],i[3]))
        print("End errors: ", len(sbc.end_error))
        for i in sbc.end_error:
            print("Error: {} {} ends at {} instead of annotated {}".format(i[0],i[1],i[2],i[3]))
