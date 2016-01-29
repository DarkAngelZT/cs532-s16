#! /bin/bash
curl -i -d "Comments=This%20is
Zetan's
test%20line" -d "box=yes" http://www.cs.tut.fi/cgi-bin/run/~jkorpela/echo.cgi | iconv -f ISO-8859-1 -t utf8 -o a1_p1_result.html
