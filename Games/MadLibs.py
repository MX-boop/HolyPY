def takeinput(mes: str):
    input(print(mes))


MadArray = [takeinput(mes="Verb-ing"), takeinput(mes="Adverb"), takeinput(mes="Adjective"), takeinput(mes="Verbing"), takeinput(mes="First Names"), takeinput(mes="First Name"), takeinput(mes="First Name"), takeinput(mes="Place"), takeinput(mes="Adj"), takeinput(mes="Noun"), takeinput(mes="Color"), takeinput(mes="Noun"), takeinput(mes="Verb"), takeinput(mes="Food"), takeinput(mes="Food"), takeinput(mes="Verb"), takeinput(mes="Verb"), takeinput(mes="Part of body"), takeinput(mes="Animal"), takeinput(mes="Verb"), takeinput(mes="Noun"), takeinput(mes="Verb-ing"), takeinput("Verb-ing"), takeinput(mes="Verb-ing"), takeinput(mes="Adj")]
# I wrote this while extremly tired
print(
    "I\'m{0}a{1}party for my birthday. I\'m{2}my best friends, like{3}and{4}and{5}The party will be at the{6}with{7}{8}and{9}{10}for decorations. First, we will{11}some snacks, like{12}and{13}, and then we will{14}some party games, like{15}the{16}on the{17}and{18}the{19}. Then comes my favorite part:{20}Happy Birthday,{21}presents and{22}some{23}cake.".format(
        MadArray[0], MadArray[1], MadArray[2], MadArray[3], MadArray[4], MadArray[5], MadArray[6], MadArray[7],
        MadArray[8], MadArray[9], MadArray[10], MadArray[11], MadArray[12], MadArray[13], MadArray[14], MadArray[15],
        MadArray[16], MadArray[17], MadArray[18], MadArray[19], MadArray[20], MadArray[21], MadArray[22], MadArray[23]))
