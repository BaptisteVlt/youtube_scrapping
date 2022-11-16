from function_scrapping_bva import *

parser = argparse.ArgumentParser()
parser.add_argument('--input', help='Input JSON file with URLs', required=True)
parser.add_argument('--output', help='Output JSON file with data', required=True)
args = parser.parse_args()
argdict = vars(args)
input = argdict['input']
output = argdict['output']

f = open(input)
data = json.load(f)
liste_vod_id = data['videos_id']


infos = scrapping_ytb(liste_vod_id)

json_output = json.dumps(infos, indent=4)

with open(output, "w") as outfile:
    outfile.write(json_output)