import islpy as isl

def mkDepGraph(Sini, Read, Write):
    RAW    = isl.UnionMap.apply_range( Read,  isl.UnionMap.reverse(Write) )
    WAW    = isl.UnionMap.apply_range( Write, isl.UnionMap.reverse(Write) )
    WAR    = isl.UnionMap.apply_range( Write, isl.UnionMap.reverse(Read)  )
    S_lt_S = isl.UnionMap.lex_lt_union_map(Sini, Sini)
    Dep    = isl.UnionMap.intersect( isl.UnionMap.union(RAW, isl.UnionMap.union(WAW, WAR)), S_lt_S )
    return Dep;

def checkTimeDepsPreserved(Snew, Dep):
    ### src2sinktime = Snew o R
    src2sinktime = isl.UnionMap.apply_range(Dep, Snew) 
    ### timesrcsink = Snew o R o Snew^{-1}
    timesrcsink  = isl.UnionMap.apply_range(isl.UnionMap.reverse(Snew), src2sinktime) 

    Tnew  = Snew.range()
    #print(Tnew)
    Sdesc = Tnew.lex_ge_union_set(Tnew)
    src_gt_sink = timesrcsink.intersect(Sdesc);
    null_map = isl.UnionMap("[N]->{  }")
    is_empty = src_gt_sink.__eq__(null_map)
    return (timesrcsink, is_empty);
    #return (timesrcsink, isl.UnionMap.empty(src_gt_sink))  # raise IslTypeError("space is not a Space")

def checkTimeDepsPreserved0(Snew, Dep):
    src2sinktime = isl.UnionMap.apply_range(Dep, Snew) ### Snew o R
    timesrcsink  = isl.UnionMap.apply_range(isl.UnionMap.reverse(Snew), src2sinktime)

    Tnew  = Snew.range()
    L = Tnew.lex_lt_union_set(Tnew)
    after = L.apply_domain(Snew).apply_range(Snew.reverse())
    print("AFTER:");
    print(L);
    is_empty = Dep.is_subset(after)
    return (timesrcsink, is_empty);

