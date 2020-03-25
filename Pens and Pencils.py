from math import ceil

t=int(input());
for x in range(t):
    values=input();
    numlec, numclas, limitpen, limitpencil, caselimit = values.split();
    numlec=int(numlec); numclas=int(numclas); limitpen=int(limitpen); limitpencil=int(limitpencil); caselimit=int(caselimit);
    if (numlec>limitpen):
        neededpens=ceil(numlec/limitpen);
    else:
        neededpens=1;
    if (numclas>limitpencil):
        neededpencils=ceil(numclas/limitpencil);
    else:
        neededpencils=1;

    if (neededpens+neededpencils<=caselimit):
        print(neededpens, neededpencils);
    else:
        print("-1");