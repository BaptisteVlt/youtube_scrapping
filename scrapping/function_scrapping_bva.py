import requests
from bs4 import BeautifulSoup as bs # importing BeautifulSoup
import re
import json
import argparse
import sys


def get_titre_chaine_desc_id(soup):
  # Titre, nom de la chaine, description, id vidéo

  data = re.search(r"var ytInitialPlayerResponse = ({.*?});", soup.prettify()).group(1)
  data = json.loads(data)


  titre = data['videoDetails']['title']
  chaine = data['videoDetails']['author']
  description = data['videoDetails']['shortDescription']
  id_vod = data['videoDetails']['videoId']
  external_link = re.findall(r'(https?://\S+)', description)

  return titre, chaine, description, id_vod, external_link

def get_likes(soup):
  data2 = re.search(r"var ytInitialData = ({.*?});", soup.prettify()).group(1)
  data2 = json.loads(data2)
  videoPrimaryInfoRenderer = data2['contents']['twoColumnWatchNextResults']['results']['results']['contents'][0]['videoPrimaryInfoRenderer']

  likes_str = videoPrimaryInfoRenderer['videoActions']['menuRenderer']['topLevelButtons'][0]['segmentedLikeDislikeButtonRenderer']['likeButton']['toggleButtonRenderer']['defaultText']['accessibility']['accessibilityData']['label']
  likes = likes_str.split(' ')[0].replace(',','')

  return likes

def get_info(soup, infos):
  
  res_info = get_titre_chaine_desc_id(soup)

  infos['titre'].append(res_info[0])
  infos['chaine'].append(res_info[1])
  infos['description'].append(res_info[2])
  infos['videos_id'].append(res_info[3])
  infos['external_link'].append(res_info[4])
  infos['likes'].append(get_likes(soup))
  return True


def scrapping_ytb(liste_vod_id):

  infos = {'titre' : [],'chaine' : [], 'description' : [], 'videos_id' : [], 'external_link' : [], 'likes' : []}
  for id in liste_vod_id:
    url = 'https://www.youtube.com/watch?v=' + id
    response = requests.get(url)
    soup = bs(response.text, 'html.parser')
    get_info(soup, infos)

  return infos
