# encoding: utf8
from __future__ import unicode_literals


STOP_WORDS = set("""
а

будем будет будете будешь буду будут будучи будь будьте будто бы был была были было
быть

в вам вами вас вашем ваши вашим вашими ваших весь во вот все всё всего всей всем всём всеми всему всех всею
всея всю вся вы

да для до

его едим едят ее её ей ел ела ем ему емъ если ест есть ешь еще ещё ею

же

за зато

и из или им ими имъ их

к как кем ко когда кого ком кому комья которая которого которое которой котором
которому которою которую которые который которым которыми которых кто

ли ль

меня мне мной мною мог моги могите могла могли могло могу могут мое моё моего
моей моем моём моему моею можем может можете можешь мои мой моим моими моих
мочь мою моя мы

на нам нами нас наса наш наша наше нашего нашей нашем нашему нашею наши нашим
нашими наших нашу не него нее неё ней нем нём нему нет нею ним ними них но

о об обо один одна одни одним одними одних одно одного одной одном одному одною
одну он она оне они оно от

по при про

с сам сама сами самим самими самих само самого самом самому саму свое своё
своего своей своем своём своему своею свои свой своим своими своих свою своя
себе себя собой собою

та так также такая такие таким такими таких такого такое такой таком такому такою
такую те тебе тебя тем теми тех то тоже тобой тобою того той только том томах тому
тот тою ту ты

у уже

чего чем чём чему что чтобы чтоб

эта эти этим этими этих это этого этой этом этому этот этою эту

я
""".split())