import re,sys
import util.normalize as normalize

class Ireko:
    depth = 0
    parent = None
    
    def __init__(self,text,startbr,endbr):
        self.text = text
        self.startbr = startbr
        self.endbr = endbr

    def __str__(self):
        return self.text

    def new_child(self,text):
        child = Ireko(
            text = text,
            startbr = self.startbr,
            endbr = self.endbr
        )
        child.parent = self
        child.depth = self.depth+1
        return child
    
    def read_one_invariant(self):
        text = self.text
        invs = [self]
        length = len(text)
        for i,c in enumerate(text):
            if c in self.startbr:
                invariant = invs[0].new_child(text[i:])
                invs.insert(0,invariant)
                continue
            if c in self.endbr:
                invariant = invs[0]
                invariant.text = invariant.text[:-length+i]+self.endbr
                invs.remove(invariant)
                if len(invs)==1:
                    # print(invariant.text)
                    return invariant.text
                continue
            if c==" ":continue
            if invs[0].depth==0 :return c
        return text
        
    def reversed(self):
        ireko = Ireko(
            text = self.text[::-1],
            startbr = self.endbr,
            endbr =  self.startbr,
        )
        ireko.parent = self.parent
        ireko.depth = self.depth
        return ireko
    
    def copy(self):
        ireko = Ireko(
            text = self.text,
            startbr = self.startbr,
            endbr = self.endbr,
        )
        ireko.parent = self.parent
        ireko.depth = self.depth
        return ireko
    
    def read_mom(self):
        f = re.search("/",self.text)
        after_Ireko = self.copy()
        after_Ireko.text = self.text[f.start()+1:]
        mom = after_Ireko.read_one_invariant()
        return mom
    
    def read_child(self):
        f = re.search("/",self.text)
        before_Ireko = self.copy()
        before_Ireko.text = self.text[:f.start()+1]
        reversed_Ideko = before_Ireko.reversed()
        mom = reversed_Ideko.read_mom()
        child = mom[::-1]
        return child
    
def transform_dint(text,startbr,endbr):
    m = re.search("\\\\dint",text)
    if not m: return text
    ireko = Ireko(
        text = text[m.end():],
        startbr = startbr,
        endbr = endbr
    )
    low = ireko.read_one_invariant()
    ireko.text = ireko.text[len(low):]
    high = ireko.read_one_invariant()
    text = text.replace("\\dint"+low+high,"\\displaystyle\\int_"+low+"^"+high)
    text = transform_dint(text,startbr,endbr)
    # print(target[:20].replace(low+high,"\\displaystyle\\int_"+low+"^"+high))
    return text




def itemize_to_ol(text):
    text = re.sub("\\\\beda<[0-9]>","<ol>",text)
    text = text.replace("\\beda","<ol>").replace("\\eeda","</ol>")
    text = text.replace("\\benu","<ol>").replace("\\eenu","</ol>")
    text = text.replace("\\begin{itemize}","<ol>").replace("\\end{itemize}","</ol>")
    text = text.replace("\\begin{enumerate}","<ol>").replace("\\end{enumerate}","</ol>")
    text = text.replace("\\begin{description}","<ol>").replace("\\end{description}","</ol>")
    text = text.replace("<ol>","<ol class = 'small-question'>")
    if not len(re.findall("<ol.*>",text))==len(re.findall("</ol>",text)):
        print("ol???????????????????????????\n%s" % text)
        sys.exit()
    return text

def item_to_li(text):
    if not re.search("\\\\item",text):
        return text
    lines = text.split("\n")
    for i,line in enumerate(lines):
        # print(line)
        if re.match("\\\\item",line):
            line = re.sub("\\\\item","",line)
            lines[i] = "<li>%s</li>" % line
    # print(lines)
    text = "\n".join(lines)
    text = text.replace("<li>[(???)]","<li class ='unorder'>(*) ")
    text = re.sub("<li>\[\([\d]\)\]","<li> ",text)
    text = re.sub("<li>\[([^\s]+)\]","<li class='unorder'> \\1 ",text)
    if not len(re.findall("<li.*>",text))==len(re.findall("</li>",text)):
        print("li???????????????????????????\n%s" % text)
        sys.exit()
    return text

def transform_frac(text):
    f = re.search("/",text)
    if not f: return text
    # print(self.text)
    if text[f.start()-1] == "}" or text[f.end()+1] == "{":
        # print(text)
        ireko = Ireko(text=text,startbr="{",endbr="}")
    else:
        ireko = Ireko(text=text,startbr="(",endbr=")")
    mom = ireko.read_mom()
    child = ireko.read_child()
    frac = "\\displaystyle\\frac{%s}{%s}" % (child,mom)
    # print(frac)
    text = text.replace("%s/%s" % (child,mom),frac)
    # print("transform_frac ??????????????????")
    return transform_frac(text)

def remove_displaystyle(text):
    if not re.search("(?:\^|\_)\{\s*-?\\\\displaystyle",text):
        return text
    text = re.sub("(\^|\_)\{\s*-?\\\\displaystyle","\\1{",text)
    return remove_displaystyle(text)

def transform_sqrt(text):
    s = re.search("???",text)
    if not s: return text
    superNum = ["??","???","???","???","???","???","???"]
    for i,n in enumerate(superNum):
        text = text.replace("%s???" % n,"\\sqrt[%s]" % str(i+3))
    text = text.replace("???","\\sqrt ")
    return text

def add_left_right(text):
    s = re.search("(?<!left)\([^???-??????-??????-???]*?\)",text)
    if not s: return text
    # print(self.text)
    ireko = Ireko(text=text,startbr="(",endbr=")")
    ireko.text = ireko.text[s.start():]
    inv = ireko.read_one_invariant()
    # print(inv)
    content = inv[1:-1]
    # print(content)
    # input("Please enter")
    added_left_right = "\\left(%s\\right)" % content
    # print(added_left_right)
    text = text.replace(inv,added_left_right)
    return add_left_right(text)

def translate(rule):
    for r in rule:
        text = text.replace(r[0],r[1])
    return text

def text_to_tex(text):
    text = re.sub("([0-9]{2,})","{\\1}",text)
    text = text.replace("???","").replace(" ","")
    text = text.replace("\r","")
    text = text.replace("\n ","\n")
    text = text.replace("\n\n","\n")
    texts = re.split("(?:\n|^)\([\d\w]\)",text)
    # texts = re.split("\n",text)
    newtexts = []
    for text in texts:
        lines = text.split("\n")
        newlines = [
            line_to_tex(line)
            for line in lines
        ]
        newtexts += ["\n".join(newlines)]
    question = newtexts[0]
    if len(newtexts)>1:
        question = newtexts[0]
        for i,text in enumerate(newtexts[1:]):
            question += "\n(%s) %s" % (i+1,text)
    text = question
    return text


FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER = []
FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER += [["???","\\{"],["???","\\}"]]
superNum = ["???","??","??","??","???","???","???","???","???","???"]
subNum = ["???","???","???","???","???","???","???","???","???","???"]
cricNum = ["???","???","???","???","???","???","???","???","???","???"]
for i,n in enumerate(superNum):
    FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER += [[n,"^%s" % i]]
for i,n in enumerate(subNum):
    FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER += [[n,"_%s" % i]]
for i,n in enumerate(cricNum):
    FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER += [[n,"\\raise0.2ex\hbox{\\textcircled{\\scriptsize{%s}}}" % i]]
FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER += [["???","^n"],["???","^-"],["???","^+"],["???","_x"],["???","_a"]]
FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER += [["???","'"],["???","*"],["???","\\fbox{\\phantom{J}}"]]
FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER += [["???","\\leqq "],["???","\\geqq "],["???","\\neq "],["???","\\to "],["???","-"]]
FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER += [["\\vec","\\overrightarrow "],["???","\iff "]]
FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER += [["??","\\pi "],["??","\\alpha "],["??","\\beta "],["??","\\gamma"],["??","\\theta "]]
FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER += [["???","\\angle "],["???","\\triangle "],["???","^\\circ "],["??","^\\circ "]]
FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER += [["log","\\log "],["sin","\\sin "],["cos","\\cos "],["tan","\\tan "]]
FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER += [["lim","\\displaystyle\\lim"],["???","\\displaystyle\\int"],["???","\\displaystyle\\sum"],["??","\\displaystyle\\sum"],["???","\\infty "]]
FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER += [["nCr","_n\\text{C}_r"],["nCk","_n\\text{C}_k"]]
FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER += [["?????????","\\cdots "],["???","\\cdot "],["??","\\cdot "],["?????????","\\cdots "],["???","\\cdot "],["???","\\cdots "]]

def line_to_tex(line):
    line = line.replace("???","").replace(" ","")
    line = normalize.join_diacritic(line)
    line = re.sub("([^???-??????-??????-??????])(?:???|\,)", "\\1,\\\;",line)
    line = re.sub("([???-??????-??????-?????????]),", "\\1???",line)
    line = re.sub("([???-??????-??????-?????????])\.", "\\1???",line)
    line = re.sub("([???-??????-??????-?????????])???", "\\1???",line)
    line = re.sub("([^???-??????-??????-?????????????????????]+)", " $\\1$ ",line)

    line = re.sub("([A-Z]{2,})","\\\\text{\\1}",line)
    line = re.sub("([A-Z^P])\s?\(","\\\\text{\\1}(",line)
    line = re.sub("???(.?)\s\$([A-Z])","???\\1 $\\\\text{\\2}",line)
    line = re.sub("???(.?)\s\$([A-Z])","???\\1 $\\\\text{\\2}",line)
    line = re.sub("????????????\s?\$(\\\\text\{[A-Z]{2}\})","$\\\\overrightarrow{\\1} ",line)
    line = re.sub("????????????\s?\$([a-z])"," $\\\\overrightarrow{\\1}",line)
    line = re.sub("(_\{.*\})C(_\{.*\})","\\1\\\\text{C}\\2",line)
    line = re.sub("\|([^???-??????-??????-?????????]*?)\|","\\\\left|\\1\\\\right|",line)
    line = re.sub("\$Lv\.(\d)\$","Lv.\\1",line)
    line = transform_frac(line)
    line = transform_sqrt(line)
    line = add_left_right(line)
    line = remove_displaystyle(line)
    for r in FROM_VIDEO_DESCRIPTION_TO_TEX_LETTER:
        line = line.replace(r[0],r[1])
    line = re.sub("\^(.)\^(.)\^(.)\^(.)", "^{\\1\\2\\3\\4}",line)
    line = re.sub("\^(.)\^(.)\^(.)", "^{\\1\\2\\3}",line)
    line = re.sub("\^(.)\^(.)", "^{\\1\\2}",line)
    line = re.sub("\_(.)\_(.)\_(.)", "_{\\1\\2\\3}",line)
    line = re.sub("\_(.)\_(.)", "_{\\1\\2}",line)
    return line

def transform_to_html_list(text):
    text = text.replace("???","&lt;").replace("???","&gt;")
    texts = re.split("\n\([\d\w]\)",text)
    question = texts[0]
    if len(texts)>1:
        question = texts[0]+"\n<ol class = 'small-question'>"
        for text in texts[1:]:
            question += "\n <li>%s</li>" % text
        question += "\n</ol>"
    return question

def transform_to_enumerate_list(text):
    texts = re.split("\n\([\d\w]\)",text)
    question =  texts[0]
    if len(texts)==1:return question
    items = "\n".join(["\\item%s" % text for text in texts[1:]])
    item_max_length = max(len(re.findall("[\d\w???-??????-??????-?????????]",texts[i+1])) for i in range(len(texts)-1))
    item_num = len(texts)-1
    if item_max_length<10:
        question = """%s\n\\begin{edaenumerate}<%s>\n%s\n\\end{edaenumerate}\n""" % (texts[0],item_num,items)
    else:
        question = """%s\n\\begin{enumerate}\n%s\n\\end{enumerate}\n""" % (texts[0],items)
    text = question
    return text

def take_linebraek_if_list(text):
    texts = re.split("(?:\n|^)\([\d\w]\)",text)
    print("text:%s" % text)
    if len(texts)==1:return text
    items = "\n".join(["(%s) %s\\\\" % (i+1,text) for i,text in enumerate(texts[1:])])
    if not texts[0]:
        return "%s\n" % items
    return "%s\\\\\n%s\n" % (texts[0],items)

def make_math_line(text):
    lines =  text.split("\n")
    for i,line in enumerate(lines):
        if re.match("\s\$\([\d\w]\)",line):continue #(1)????????????????????????????????????
        lines[i] = re.sub("^\s\$([^???-??????-??????-?????????]+)\$\s$","\\[\\1\\]",line)
    question = "\n".join(lines)
    return question

def make_array(text):
    text = re.sub("\\\\\[(.*)\\\\\]\n\\\\\[(.*)\\\\\]\n\\\\\[(.*)\\\\\]\n\\\\\[(.*)\\\\\]","\[\\\\left\\{\\\\begin{array}{l}\\1\\\\\\\\ \\2\\\\\\\\ \\3\\\\\\\\ \\4\\\\end{array}\\\\right.\]",text)
    text = re.sub("\\\\\[(.*)\\\\\]\n\\\\\[(.*)\\\\\]\n\\\\\[(.*)\\\\\]","\[\\\\left\\{\\\\begin{array}{l}\\1\\\\\\\\ \\2\\\\\\\\ \\3\\\\end{array}\\\\right.\]",text)
    text = re.sub("\\\\\[(.*)\\\\\]\n\\\\\[(.*)\\\\\]","\[\\\\left\\{\\\\begin{array}{l}\\1\\\\\\\\ \\2\\\\end{array}\\\\right.\]",text)
    return text

def tex_to_mytex(text):
    text = text.replace("???","<").replace("???",">")
    text = text.replace("$ ","$").replace(" $","$")
    text = text.replace("\\displaystyle\\frac","\\bunsuu")
    text = text.replace("\\overrightarrow","\\vv")
    text = re.sub("\\\\left\|(.*?)\\\\right\|","\\\\zettaiti{\\1}",text)
    text = re.sub("\\\\\[(.*?)\\\\\]","\n\\\\vspace{0.3zw}\n\\\\hspace{0.5zw}$\\1\\\\vspace{0.3zw}$\n\n",text)
    return text