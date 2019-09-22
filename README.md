# tawqeeTeX

_tawqeeTeX_ is a LaTeX prayer time schedule generator.

![screenshot](https://imgur.com/9w8Tsnw.png =500)

## Dependencies
* [python3](https://www.python.org/downloads/)
* [pylatex](https://pypi.org/project/PyLaTeX/) (use pip3)

Also, you will need to install a TeX compiler if you don't have one (I recommend _pdflatex_)

## How to use tawqeeTeX

To start the generation of the schedule you need to fill these parameters:
* city
* country
* month
* year

Here is an exemple:

```bash
$ python3 tawqeeTeX.py Milano Italy 09 2019
```

_tawqeeTeX_ allows you to configure the generation of the time schedule setting other parameters such as:
* language
* calculation method
* hijri calendar adjustment

For example:

```bash
$ python3 tawqeeTeX.py Milano Italy 09 2019 --language it --method 1 --adj 1
```

This configuration will create a time schedule in italian using the MWL (Muslim World League) method. The adjustment
will simply apply an offset of day on the hijri calendar (negative offsets are accepted too).

Enter the following command in order to display a menu that includes a brief description of all available options:

```bash
$ python3 tawqeeTeX.py --help
```

## Output

_tawqeeTeX_ will automatically create a .pdf document named [city]-[month]-[year].pdf
A .tex file with the same name is also provided in order to give users the possibility to customize theirs tables.

## Credits

I would like to thank [Islamic Network](https://github.com/islamic-network) for [Al-Adhan API](https://github.com/islamic-network/api.aladhan.com) on which I based this project.

## Contact

<tawqeeTeX@gmail.com>
