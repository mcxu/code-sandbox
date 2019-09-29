"""
4. Median of Two Sorted Arrays [Hard]

There are two sorted arrays nums1 and nums2 of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).
You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5
"""

class P4:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        merged = []
        #print("nums1:{}, nums2:{}".format(nums1, nums2))
        # create merged list
        if(len(nums1)!=0 and len(nums2)!=0):
            i = 0; j = 0
            while(i<len(nums1) and j<len(nums2)):
                #print("i={}, j={}, nums1 val={}, nums2 val={}".format(i,j,nums1[i],nums2[j]))
                
                if(nums1[i] < nums2[j]):
                    merged.append(nums1[i])
                    i+=1
                    if(i == len(nums1)):
                        for k in range(j,len(nums2)):
                            merged.append(nums2[k])
                            j = k
                elif(nums1[i] >= nums2[j]):
                    merged.append(nums2[j])
                    j+=1
                    if(j == len(nums2)):
                        for k in range(i,len(nums1)):
                            merged.append(nums1[k])
                            i = k
                
                #print(" nums1:{}, nums2:{}".format(nums1,nums2))
                #print(" merged:{}".format(merged))
        
        #print("final merged list: {}".format(merged))
        
        # if one of lists is empty
        if(len(nums1)==0):
            merged = nums2
        elif(len(nums2)==0):
            merged = nums1
        
        #print("final merged after empty check: {}".format(merged))
        
        # find median
        lo_ind = int((len(merged)-1)/2)
        median = float(merged[lo_ind])
        #print("assuming odd number of nums in merged. median: {}".format(median))
        if(len(merged) % 2 == 0):
            median = float(median + merged[lo_ind+1])/2
            #print("even number of nums in merged. median: {}".format(median))
    
        return median

    
    def test_findMedianSortedArrays(self):
        array_pairs = [
            [
                [1,3,5,7,9],
                [2,4,10,11,13,17,21]
            ],
            [
                [1,2],
                [3,4]
            ],
            [
                [5,7,8,12,15],
                [1,2,4,5,6,7,9,15,18,22]
            ],
            [
                [76,89,104,287,566,596,660,719,879,1012,1080,1225,1304,1568,1898,1959,1965,2140,2276,2395,2634,2764,2801,2877,3009,3010,3188,3318,3356,3459,3549,3586,3793,3844,3890,4297,4328,4423,4494,4546,4570,4613,4616,4630,4680,4807,5002,5237,5245,5312,5345,5489,5606,5731,5732,5796,5816,6116,6197,6201,6204,6303,6339,6357,6395,6412,6445,6552,6584,6612,6678,6823,6825,6892,7272,7311,7534,7535,7686,7891,8032,8112,8120,8226,8239,8578,8583,8807,9214,9317,9384,9388,9447,9484,9611,9739,9753,9812,9838,9854,9905,9936,9944,9978,10033,10346,10356,10581,10583,10755,10764,10819,10845,11040,11049,11111,11169,11183,11249,11597,11640,11739,11743,11856,11925,11950,11991,12086,12175,12531,12551,12581,12721,12987,13101,13176,13259,13342,13401,13550,13635,13657,13713,13981,14014,14032,14039,14093,14152,14205,14322,14339,14361,14444,14449,14471,14536,14600,14661,14892,15034,15313,15399,15530,15553,15653,15723,15734,15767,15811,16002,16057,16066,16182,16453,16540,16629,16924,16946,17323,17339,17362,17416,17466,17629,17769,17978,17985,18262,18417,18485,18555,18565,18565,18652,18687,18701,18709,18791,19076,19094,19163,19171,19195,19263,19381,19381,19432,19566,19625,19722,19738,19743,19892,19960,20124,20272,20290,20324,20405,20516,20587,20734,20808,20915,20958,20965,21069,21234,21384,21440,21441,21595,21690,21704,21710,21734,21802,21858,21956,21989,22004,22055,22102,22235,22254,22272,22283,22399,22487,22623,22646,22724,22774,22821,22825,23076,23251,23306,23477,23751,23852,24057,24123,24179,24288,24436,24529,24685,24897,25077,25116,25190,25325,25547,25552,25614,25707,25754,25824,25920,25941,25955,25962,26071,26091,26182,26193,26199,26494,26525,26535,26624,26815,26944,27031,27055,27068,27085,27207,27298,27347,27349,27388,27522,27737,27900,28046,28150,28180,28184,28253,28300,28398,28438,28615,28698,28867,28933,28959,29213,29219,29224,29279,29396,29511,29528,29632,29693,29850,29897,29972,29979,30057,30085,30115,30123,30225,30544,30550,30770,30787,30823,31070,31259,31324,31714,31971,32033,32076,32251,32319,32350,32408,32475,32681,32701,32764],
                [122,255,318,346,361,452,520,584,603,657,669,695,708,730,745,757,766,770,773,787,799,818,845,873,875,899,966,985,1103,1114,1164,1238,1243,1261,1284,1339,1351,1424,1431,1457,1468,1482,1493,1514,1584,1601,1630,1644,1683,1739,1744,1751,1793,1867,1870,1909,1912,1941,1970,2017,2137,2155,2194,2214,2236,2257,2472,2514,2548,2654,2734,2791,2798,2823,2886,2887,2919,2941,2958,2998,2999,3026,3054,3061,3174,3192,3225,3282,3358,3389,3392,3406,3427,3429,3470,3501,3555,3590,3604,3676,3718,3724,3744,3765,3796,3803,3808,3846,3883,3914,3916,4049,4092,4102,4118,4128,4159,4170,4170,4287,4296,4309,4349,4363,4374,4571,4594,4606,4621,4637,4731,4746,4775,4800,4816,4832,4837,4867,4880,4935,4942,4976,5007,5077,5106,5122,5179,5199,5237,5255,5265,5341,5370,5378,5394,5398,5467,5493,5518,5548,5630,5651,5762,5842,5867,5914,5915,5935,6013,6081,6092,6132,6178,6217,6245,6289,6409,6410,6445,6464,6478,6481,6660,6711,6711,6767,6778,6782,6788,6844,6855,6945,7036,7107,7119,7210,7229,7256,7292,7292,7355,7395,7446,7455,7472,7477,7481,7529,7558,7560,7590,7661,7669,7749,7802,7862,7886,7922,7993,8007,8009,8051,8055,8064,8071,8211,8305,8410,8443,8457,8463,8496,8629,8633,8649,8744,8745,8834,9021,9059,9081,9098,9125,9126,9136,9210,9222,9235,9318,9353,9367,9384,9475,9495,9519,9543,9596,9597,9679,9691,9705,9708,9842,9890,9905,9907,9914,9923,9932,9937,9939,10006,10015,10098,10154,10156,10183,10202,10209,10226,10229,10245,10290,10307,10361,10412,10438,10446,10450,10461,10534,10545,10651,10727,10860,10940,10970,10996,11056,11088,11091,11111,11160,11162,11216,11241,11292,11292,11465,11475,11538,11576,11696,11704,11825,11858,12014,12070,12083,12153,12163,12171,12202,12211,12225,12239,12251,12316,12549,12580,12583,12593,12702,12718,12731,12769,12813,12961,12973,13016,13027,13031,13033,13035,13082,13097,13125,13140,13143,13190,13219,13281,13283,13326,13349,13364,13394,13418,13439,13448,13451,13462,13528,13540,13616,13694,13729,13790,13800,13808,13891,13920,13943,13979,14216,14354,14371,14378,14388,14487,14530,14543,14543,14642,14712,14782,14786,14828,14829,14832,14897,14911,14914,14973,15012,15054,15080,15107,15123,15130,15149,15151,15159,15236,15262,15319,15328,15340,15372,15445,15458,15461,15568,15576,15651,15658,15670,15736,15819,15868,15871,15991,16044,16198,16229,16251,16322,16335,16364,16397,16403,16408,16417,16456,16492,16495,16562,16565,16605,16620,16644,16652,16809,16861,16908,16942,16955,17044,17061,17102,17225,17240,17335,17337,17361,17462,17469,17540,17649,17686,17728,17754,17781,17830,17874,18019,18023,18130,18133,18181,18254,18255,18281,18370,18380,18391,18398,18419,18488,18491,18520,18638,18663,18763,18857,18865,18894,18944,18956,18987,18997,19044,19067,19071,19135,19165,19277,19287,19302,19333,19347,19389,19497,19570,19587,19592,19640,19803,19872,19880,19923,19927,19946,19993,20004,20007,20088,20223,20247,20298,20376,20378,20417,20433,20439,20471,20472,20505,20527,20640,20652,20705,20726,20762,20788,20811,20814,20851,20862,20879,20909,21014,21146,21236,21273,21290,21361,21436,21466,21492,21673,21796,21831,21834,21898,21973,21991,22019,22020,22046,22046,22151,22193,22213,22244,22296,22329,22440,22444,22454,22462,22471,22518,22537,22554,22578,22647,22762,22895,22897,22946,22988,22989,22997,23035,23076,23109,23136,23325,23343,23383,23387,23437,23450,23533,23541,23562,23596,23779,23796,23820,23932,24010,24125,24142,24242,24373,24547,24560,24587,24598,24650,24737,24767,24774,24832,24868,24876,24892,24911,24947,24982,25004,25041,25115,25223,25226,25245,25384,25398,25483,25567,25607,25636,25690,25713,25728,25732,25738,25784,25811,25884,25930,25955,25959,25982,26035,26076,26093,26107,26124,26157,26192,26212,26231,26264,26302,26361,26367,26380,26422,26453,26486,26544,26580,26770,26785,26804,26851,26880,26972,26977,27025,27041,27096,27098,27182,27202,27235,27284,27349,27372,27396,27454,27511,27529,27537,27598,27719,27736,27832,27860,27864,27884,27917,27934,27948,28039,28041,28042,28043,28050,28074,28100,28106,28123,28162,28195,28367,28422,28453,28505,28541,28566,28595,28596,28605,28615,28640,28641,28652,28657,28667,28696,28740,28759,28779,28803,28832,28845,28852,28854,28864,28932,28950,29042,29047,29085,29147,29218,29230,29244,29288,29332,29363,29376,29440,29458,29465,29467,29492,29493,29534,29558,29560,29601,29612,29663,29740,29793,29817,29887,29906,30106,30206,30231,30276,30297,30331,30364,30378,30425,30431,30565,30588,30603,30613,30646,30663,30694,30712,30726,30772,30774,30846,30896,30955,31055,31075,31110,31134,31146,31228,31259,31269,31271,31302,31334,31392,31446,31511,31516,31518,31562,31721,31779,31813,31849,31865,31866,31906,31906,31934,31941,31954,32015,32083,32150,32205,32232,32267,32268,32294,32351,32373,32396,32400,32405,32452,32479,32480,32487,32491,32491,32561,32590,32605,32641,32716,32757]
            ]
        ]

        for pair_obj in array_pairs:
            l1 = pair_obj[0]
            l2 = pair_obj[1]
            median = self.findMedianSortedArrays(l1,l2)
            print("test_findMedianSortedArrays:     l1:{}, l2:{}, median:{}".format(l1,l2,median))


def main():
    p4 =  P4()
    p4.test_findMedianSortedArrays()

if __name__ == "__main__":
    main()