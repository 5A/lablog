"""
NOTE: This script cannot be run in this directory because it needs packages in its
parent folder, and we don't want to mess up with paths. 
Just ipython in lablog root dir and copy paste enter
"""

import random
from backend.lablog import Lablog
from tests.lorem import get_sentence

a = Lablog()

catagories = [
    "Science",
    "Technology",
    "Game",
    "Life",
    "Literature",
    "Mathematics",
    "Miscellaneous"
]

all_tags = [
    "Hardware",
    "Software",
    "Embedded",
    "Optics",
    "Chemistry",
    "Mechanics",
    "Productivity",
    "Robots and Motors",
    "Art",
    "Cooking",
    "Data",
    "Health",
    "Microfluidics",
    "Radiation",
    "Scripts",
    "Semiconductor",
    "Toy",
    "Traval",
    "Physics",
    "Web",
    "Utility"
]

# generate posts
for i in range(514):
    catagory = catagories[random.randint(0, len(catagories)-1)]
    tags = random.sample(all_tags, random.randint(0, 5))
    post_title = get_sentence(1) + " {}, Generated Test Post Title".format(i)
    post_abstract = get_sentence(random.randint(
        4, 8)) + " This is Abstract {}. Post catagory: {}, Post tags: {}.".format(i, catagory, tags)
    post_link = "/posts/{}.html".format(i)
    a.add_post(post_title, post_abstract, post_link,
               catagory=catagory, tags=tags)

a.serialize_to_file("./tests/data/blogdata.json")
