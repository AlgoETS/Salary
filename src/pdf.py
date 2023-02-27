# -*- coding: utf-8 -*-
import re
from operator import itemgetter

import fitz


def fonts(doc, granularity=False):
    """Extracts fonts and their usage in PDF documents.
    :param doc: PDF document to iterate through
    :type doc: <class 'fitz.fitz.Document'>
    :param granularity: also use 'font', 'flags' and 'color' to discriminate text
    :type granularity: bool
    :rtype: [(font_size, count), (font_size, count}], dict
    :return: most used fonts sorted by count, font style information
    """
    styles = {}
    font_counts = {}

    for page in doc:
        # print(dir(page))
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:  # iterate through the text blocks
            if b["type"] == 0:  # block contains text
                for l in b["lines"]:  # iterate through the text lines
                    for s in l["spans"]:  # iterate through the text spans
                        if granularity:
                            identifier = (
                                f"{s['size']}_{s['flags']}_{s['font']}_{s['color']}"
                            )
                            styles[identifier] = {
                                "size": s["size"],
                                "flags": s["flags"],
                                "font": s["font"],
                                "color": s["color"],
                            }
                        else:
                            identifier = str(s["size"])
                            styles[identifier] = {"size": s["size"], "font": s["font"]}

                        font_counts[identifier] = (
                            font_counts.get(identifier, 0) + 1
                        )  # count the fonts usage

    font_counts = sorted(font_counts.items(), key=itemgetter(1), reverse=True)

    if len(font_counts) < 1:
        raise ValueError("Zero discriminating fonts found!")

    return font_counts, styles


def font_tags(font_counts, styles):
    """Returns dictionary with font sizes as keys and tags as value.
    :param font_counts: (font_size, count) for all fonts occurring in document
    :type font_counts: list
    :param styles: all styles found in the document
    :type styles: dict
    :rtype: dict
    :return: all element tags based on font-sizes
    """
    p_style = styles[
        font_counts[0][0]
    ]  # get style for most used font by count (paragraph)
    p_size = p_style["size"]  # get the paragraph's size

    # sorting the font sizes high to low, so that we can append the right integer to each tag
    font_sizes = sorted(
        map(float, [font_size for font_size, count in font_counts]), reverse=True
    )

    # aggregating the tags for each font size
    idx = 0
    size_tag = {}
    for size in font_sizes:
        idx += 1
        if size == p_size:
            idx = 0
            size_tag[size] = "<p>"
        if size > p_size:
            size_tag[size] = f"<h{idx}>"
        elif size < p_size:
            size_tag[size] = f"<s{idx}>"

    return size_tag


def headers_para(doc, size_tag):
    """Scrapes headers & paragraphs from PDF and return texts with element tags.
    :param doc: PDF document to iterate through
    :type doc: <class 'fitz.fitz.Document'>
    :param size_tag: textual element tags for each size
    :type size_tag: dict
    :rtype: list
    :return: texts with pre-prended element tags
    """
    header_para = []  # list with headers and paragraphs
    first = True  # boolean operator for first header
    previous_s = {}  # previous span

    for page in doc:
        blocks = page.get_text("dict")["blocks"]
        for b in blocks:  # iterate through the text blocks
            if b["type"] == 0:  # this block contains text
                # REMEMBER: multiple fonts and sizes are possible IN one block

                block_string = ""  # text found in block
                for l in b["lines"]:  # iterate through the text lines
                    for s in l["spans"]:  # iterate through the text spans
                        if s["text"].strip():
                            if first:
                                first = False
                                previous_s = s
                                block_string = size_tag[s["size"]] + s["text"]
                            else:
                                if s["size"] == previous_s["size"]:
                                    if block_string and all(
                                        (c == "|") for c in block_string
                                    ):
                                        # block_string only contains pipes
                                        block_string = size_tag[s["size"]] + s["text"]
                                    if block_string == "":
                                        # new block has started, so append size tag
                                        block_string = size_tag[s["size"]] + s["text"]
                                    else:  # in the same block, so concatenate strings
                                        block_string += " " + s["text"]

                                else:
                                    header_para.append(block_string)
                                    block_string = size_tag[s["size"]] + s["text"]

                                previous_s = s

                    # new block started, indicating with a pipe
                    block_string += "|"

                header_para.append(block_string)

    return header_para


if __name__ == "__main__":
    # Open the PDF file
    doc = fitz.open("./data/2023_salary_guide.pdf")
    print(doc)
    font_counts, styles = fonts(doc, granularity=False)
    size_tag = font_tags(font_counts, styles)
    print(size_tag)
    header_para = headers_para(doc, size_tag)

    # find all h1 tags
    h1 = [i for i in header_para if "<h1>" in i]
    pattern = "(?<=<h1>).+?(?=</h1>)"
    # r'<h1>(.*?)\|'

    regions = []
    for line in h1:
        region = re.findall(r"<h1>(.*?)\|", line)
        regions.extend(region)
    print(regions)

    # save the output to a text file
    with open("output.txt", "w") as f:
        for item in header_para:
            f.write(f"{item} ")
