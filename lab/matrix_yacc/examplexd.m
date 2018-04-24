aaaa = 1;
bbbb = 2;
dddd = 3;
eeee = zeros(5);
ffff = ones(7);
gggg = eye(9);
float = 1.1;
matrix = [ 1.0, 2;
           1, 3;
           1, 4 ] ;
matrix[1] = 7;

if(N==10)
    print "N==10";
else if(N!=10)
    print "N!=10";

if(N>5)
    print "N>5";
else if(N>=0)
    print "N>=0";

if(N<10)
    print "N<10";
else if(N<=15)
    print "N<=15";

while(k>0) {
    if(k<5)
        i = 1;
    else if(k<10)
        i = 2;
    else
        i = 3;

    #k = k - 1;
}

for i = 1:N {
    if(i<=N)
        print i;
    else if(i<=N)
        break;
    else
        continue;
}