#!/usr/bin/env python
# -*- coding: utf-8 -*-  
'''
Created on 2014年8月27日

@author: ezonghu
'''

TCs = [ ({"-10 0 10 0","0 -10 0 10"}, 1),
       
 ({"-10 0 0 0","0 0 10 0","0 -10 0 0","0 0 0 10"}, 1),
 
 ({"-10 0 0 0","0 0 10 0","0 -10 0 0","0 0 0 10"}, 4),
 
 ({"0 0 1 0",   "2 0 4 0",   "5 0 8 0",   "9 0 13 0",
 "0 1 1 1",   "2 1 4 1",   "5 1 8 1",   "9 1 13 1",
 "0 0 0 1",   "1 0 1 1",   "2 0 2 1",   "3 0 3 1",
 "4 0 4 1",   "5 0 5 1",   "6 0 6 1",   "7 0 7 1",
 "8 0 8 1",   "9 0 9 1",   "10 0 10 1", "11 0 11 1",
 "12 0 12 1", "13 0 13 1"}, 1),
    
({"-2 6 -2 1",  "2 6 2 1",  "6 -2 1 -2",  "6 2 1 2",
 "-2 5 -2 -1", "2 5 2 -1", "5 -2 -1 -2", "5 2 -1 2",
 "-2 1 -2 -5", "2 1 2 -5", "1 -2 -5 -2", "1 2 -5 2",
 "-2 -1 -2 -6","2 -1 2 -6","-1 -2 -6 -2","-1 2 -6 2"}, 5),
       
({"-252927 -1000000 -252927 549481","628981 580961 -971965 580961",
"159038 -171934 159038 -420875","159038 923907 159038 418077",
"1000000 1000000 -909294 1000000","1000000 -420875 1000000 66849",
"1000000 -171934 628981 -171934","411096 66849 411096 -420875",
"-1000000 -420875 -396104 -420875","1000000 1000000 159038 1000000",
"411096 66849 411096 521448","-971965 580961 -909294 580961",
"159038 66849 159038 -1000000","-971965 1000000 725240 1000000",
"-396104 -420875 -396104 -171934","-909294 521448 628981 521448",
"-909294 1000000 -909294 -1000000","628981 1000000 -909294 1000000",
"628981 418077 -396104 418077","-971965 -420875 159038 -420875",
"1000000 -1000000 -396104 -1000000","-971965 66849 159038 66849",
"-909294 418077 1000000 418077","-909294 418077 411096 418077",
"725240 521448 725240 418077","-252927 -1000000 -1000000 -1000000",
"411096 549481 -1000000 549481","628981 -171934 628981 923907",
"-1000000 66849 -1000000 521448","-396104 66849 -396104 1000000",
"628981 -1000000 628981 521448","-971965 521448 -396104 521448",
"-1000000 418077 1000000 418077","-1000000 521448 -252927 521448",
"725240 -420875 725240 -1000000","-1000000 549481 -1000000 -420875",
"159038 521448 -396104 521448","-1000000 521448 -252927 521448",
"628981 580961 628981 549481","628981 -1000000 628981 521448",
"1000000 66849 1000000 -171934","-396104 66849 159038 66849",
"1000000 66849 -396104 66849","628981 1000000 628981 521448",
"-252927 923907 -252927 580961","1000000 549481 -971965 549481",
"-909294 66849 628981 66849","-252927 418077 628981 418077",
"159038 -171934 -909294 -171934","-252927 549481 159038 549481"},
824759),
] 

