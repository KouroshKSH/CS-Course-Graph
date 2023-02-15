# CS-Course-Graph
This repository creates an [Obsidian](https://obsidian.md/) graph that connects the [Computer Science](https://cs.sabanciuniv.edu/) courses offered at [Sabanci University](https://www.sabanciuniv.edu/). The project is a combination of a web scraper written by [Arya Hassibi](https://github.com/aryahassibi), and a script for creating markdown files by me.

---

## Goal
Ours main aim of doing this was to assist the undergraduate Sabanci students, and make the process of choosing their CS courses easier. A visual representation of all courses can greatly help anyone to plan accordingly, and avoid any unnecessary hassle later on.

---

## How it Works
First, the courses and their related information were scraped from [this](http://suis.sabanciuniv.edu/prod/sabanci_www.p_get_courses?coll_code=E&levl_code=UG&subj_code=CS&lang=eng) website by Arya using [Beautiful Soup](https://beautiful-soup-4.readthedocs.io/en/latest/#). He then cleaned them, and divided the data gathered in to 5 main sections: 
0. Course name & its code
1. Prerequisite
2. Corequisite
3. ECTS Credit
4. General Requirements

Later, the database was uploaded to a Google Sheets file, which was used by me to download them as a [CSV](https://en.wikipedia.org/wiki/Comma-separated_values) file. After that, using [mdutils](https://github.com/didix21/mdutils), I generated [markdown](https://www.markdownguide.org/) files that were formatted in such a way that could be used by Obsidian to index them appropriately (_i.e._ [Backlinks](https://help.obsidian.md/Plugins/Backlinks)).

As a result, one can traverse the global/local graph(s) made automatically by Obsidian to see the interconnections between the CS courses, and find the required courses to take for a specific class, or to see what options can be unlocked after finishing that course.

---

## Contributions
Feel free to contribute to this project, modify code, or offer feedback regarding the codes written. 
