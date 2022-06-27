from numpy import sort

# Brasil: 389 elementos de 3714
# Tiempo de ejecución: 18.17 minutos
Brasil = ['---1-01011-00', '100---1--1100', '1001--1--1---', '1-01---01-1-0', '-0---0101110-', '1--11-101----', '-0-1-0-011-0-', '100-----11--0', '-00--01-11---', '-00--0--11-00', '100-1--0--10-', '-001--10111-0', '--0110-0-1--0', '-001-0-0---00', '-00--0-01--00', '----10101--00', '-001-010-----', '--0-10--1--00', '1--1--1-11100', '1-011-10-----', '-00-10-0-1--0', '--0--01-11100', '10-1--1-1--0-', '--01101-----0', '10--1---11--0', '1----0-01--00', '10---0---1-00', '1-0---101110-', '1--1-0-0-11-0', '-0---0101-100', '1001---0-1--0', '10-11-1-----0', '-0-1-0101----', '-00-10-0-1-0-', '10--1-10-110-', '----101-11100', '1-01---01--00', '-0--10--111-0', '100---10--100', '10---0--1----', '-0011--0111--', '10--1-10-1-00', '10--1--01--0-', '1---101--1---', '10-1---011-0-', '-0--101-11---', '--0-1010--100', '10-11--0---00', '-00-10---11-0', '10----101110-', '--01101--1---', '100----011-0-', '1001--1-----0', '10---0-0---00', '---110--11-00', '1001---0-1-0-', '--0-101-1----', '-001-01-----0', '-0-1-0-01--00', '1001--1----0-', '100---1-1----', '--0--01011-00', '--0-101--1100', '10-1-0----1--', '1-0-10-------', '-00--010-1-00', '-001--1-11100', '1--11--01-10-', '100-1-1--1---', '--0-10-01-10-', '1-0-1---1--00', '10-1--1-1---0', '1-0-1-10-1-00', '-00-10-0--10-', '-0011-1-1---0', '10-11-1----0-', '10---010-----', '1---1-1011--0', '1---10---1-00', '-00-1-1011--0', '1----0-01-10-', '10---01-----0', '1--1-010-1---', '1---10-0---00', '1--1-010---0-', '----10101110-', '--011-10111-0', '1-0--0--1----', '---110101----', '-00-101----0-', '1-011-1----0-', '1--1-01--11--', '100-1---1----', '10---0-0-1--0', '1----0--1110-', '1--1-01--1-0-', '-0-11-101-100', '--0-1010-11-0', '10-1-01------', '-0-110-0-1--0', '1---1-101--00', '---110--111-0', '-0011-10--100', '1--1-01---10-', '-0--10-0111--', '100-1--0--1-0', '1-0--01-----0', '1--11---1110-', '-0-1-01-1--0-', '100-1------00', '1--11--01-1-0', '10----1-11-00', '1-0-1--01---0', '--011-101-100', '10-11---1----', '-00--0-0111--', '1-0--0---1-00', '-00-10---110-', '1-0--0-0---00', '-0-11-1011-00', '-0011-1-1-1--', '-00-10-0---00', '-0--10-01---0', '1--11-10-1-00', '1----0--1-100', '100----01-10-', '1--1--1011-00', '-0011--01-10-', '1--11-1-1---0', '10--1--0111--', '1-011-----100', '1--11--011--0', '100-----1--00', '10--1---1--00', '1----01-1-1--', '1-01--1-11---', '1001-----1-00', '1-0--01----0-', '10--1---11-0-', '1---10-0-1--0', '10-11--0-1-0-', '1----0-011--0', '1-011---1----', '-00--01-1---0', '---1101-11---', '--011-1-11100', '-00-1010-----', '1--1--101-100', '-00-101--1---', '1--11---11-00', '1-01--1-1-1--', '-0---01-11100', '-0-110-0---00', '--01-0101----', '-00-10----100', '-0-110--1----', '1-01----111-0', '1-01--10-1-00', '-0--10-01-10-', '1-01--1-1---0', '-00110-------', '1-0---1011--0', '1--110-------', '---110-011--0', '-0-1101----0-', '-00-10-0--1-0', '--01-0--1-100', '1-01-01------', '10--1-10--100', '10-11-----100', '1-01-0-0-----', '1---10--1----', '-001-0---1-00', '-0--1010--100', '1-0-1-10-11-0', '100--0-------', '1--11-1-1-1--', '-00--0-01-10-', '---110-01--00', '-00-10---1-00', '-0-11010-----', '10-1---01-1-0', '100-1-1---1--', '-001-01--1---', '1---101-----0', '-0--101-1---0', '-00--01-1-1--', '1-011--0---00', '10011--------', '--0-10--1110-', '--0-1010-1-00', '1--1-0-0--100', '--0110--1----', '1-01-0------0',
          '10---01----0-', '-00--010--100', '1-01-0----1--', '1-0-1---11-0-', '--0110-0---00', '1-011--0-1-0-', '-00--0-011--0', '1001----1----', '--0-10--11--0', '-0--101--1100', '--0--0101110-', '-0011-1-11---', '-0-1-01-11---', '---1101-1--0-', '--011010-----', '10-11-10-----', '10-1--101----', '--01-010-1-00', '-0-110---1-00', '-00--0--1-100', '1----01-11---', '1-01----11-00', '-0--10-011-0-', '--01-0-01--00', '1--1-0---1100', '-00-101---1--', '1-0--0-0-1--0', '----1010111-0', '1-01-0-----0-', '10---0-0-1-0-', '1----010-1-00', '-00--0-01-1-0', '-0--10--1--00', '--0-10-011-0-', '1----0--11-00', '10---01--1---', '1-01-0---1---', '100----01---0', '1-01--1-1--0-', '-0011---1110-', '-0011-10-1-00', '10--1--01---0', '-001-0--1----', '1-01---011--0', '-00--010-11-0', '1--1-0-0-110-', '-00-1-101--00', '1-0--0-0-1-0-', '1----0-01-1-0', '10--1-1-1----', '-0011--01-1-0', '-00--01-1--0-', '1---1-101110-', '-0--10101----', '1-0-1--01--0-', '10-1--1-11---', '10-1----11-00', '-0-1101-----0', '-001-0-0-110-', '-0-11-1-11100', '-0011-1-1--0-', '--0110---1-00', '-00--0101----', '1-0-1-1-1----', '-0--10--1110-', '-0011-10-11-0', '100-1-1----0-', '1-011----1-00', '--01-0-011-0-', '1-0-1--0111--', '--0--0101-100', '100----0111--', '---1101-1---0', '1---10----100', '1-011-1-----0', '-001-0-0-1--0', '-001--101-100', '100-1-1-----0', '1---10-0--1-0', '100---10-11-0', '1--11--01--00', '100---10-1-00', '--01-01-1--0-', '1001--10-----', '-00--0-011-0-', '--011-1011-00', '-0011--011-0-', '1-011--0--1-0', '10-1---011--0', '---1101-1-1--', '100---10-110-', '1--11--011-0-', '---110-011-0-', '--0-1010-110-', '10-1-0---1---', '-00--0--111-0', '-0-11-101110-', '1-0-1---11--0', '1--1--10111-0', '10--1-10-11-0', '1----0-011-0-', '1-0-1-1--1100', '1--11-1-1--0-', '-0011-1--1100', '--0-10-01---0', '---110--1-100', '-0-1-010-1-00', '100-1-10-----', '-0-1-0-011--0', '-0---010111-0', '1---1010-----', '-0011---1--00', '1-0---101--00', '-0-11-10111-0', '1-0---1-11-00', '10-1----1-100', '10----10111-0', '10-1--1-1-1--', '-00-1-1-11-00', '1--11---1-100', '1001---0---00', '--0--010111-0', '--0110-0-1-0-', '--01-0-011--0', '1-0-1-10--100', '10--10-------', '1--1-0--1----', '1-011-1--1---', '10-1---01--00', '100-1--0-1-0-', '-00-101-----0', '-001--1011-00', '1-0--01--1---', '1-01---011-0-', '1-011--0-1--0', '1-0--0----100', '-0011---111-0', '--01-01-1---0', '10-1-0------0', '---11010-1-00', '-00-10--1----', '100-1----110-', '-0---01011-00', '-0--1010-1-00', '100-1--0-1--0', '1--1-01-----0', '10----101--00', '-00-1-1011-0-', '1--11---111-0', '-001-01----0-', '-0-1-01-1---0', '--0-10-0111--', '1-01----1-100', '1----0--111-0', '-0011--011--0', '10--1-1--1100', '1---101----0-', '-0-110-0-1-0-', '-001--101110-', '100-1----11-0', '1----01-1--0-', '-0-1101--1---', '1---10-0-1-0-', '1-01--101----', '1---1-1-11-00', '--01-01-11---', '1-0-1-10-110-', '1----01-1---0', '-0--1010-11-0', '1--1-010--1--', '10-11-1--1---', '10-11--0-1--0', '--01101----0-', '1---101---1--', '-00--01--1100', '-0011-101----', '10-1--10-1-00', '1--11-1-11---', '--011-101110-', '-00--0--1110-', '10-1-0-0-----', '10-1-0-----0-', '10-1----111-0', '-0--101-1--0-', '---110-01-1-0', '10-11----1-00', '--01-0--11-00', '100-----1110-', '100-1--0-11--', '1----0101----', '1-0--010-----', '1--1-0-0-1-00', '1---10---11-0', '-0-1-0--11-00', '-0--101-1-1--']

# Corea: 121 elementos de 2900
# Tiempo de ejecución: 10.44 minutos
Corea = ['1--1-000-0--1', '--0-1--000--1', '--011-00-----', '--01--0--0--1', '1-0-10-0--1--', '---110-0-01-1', '--0110-0--1--', '1---1-0-001--', '--011-0-0--1-', '1-01--0--0---', '--01-0-0-01--', '--0110----1-1', '--0-100------', '1-0---0--0-11', '---110--001-1', '--01-00---1--', '--011-0-----1', '--0---0--01-1', '--01-00--0---', '1----000-01-1', '1-0--00--0---', '1-01--000-1--', '1--11-0--0--1', '1--1100---1--', '1-0-1-00-----', '1-0-10-00--11', '1-0-10---0---', '-0--1-00001--', '1---1-00-0--1', '--01--00-0---', '1--110-0-0-11', '1--110---01-1', '--0-10---01--', '--0110----11-', '----1000-0---', '1-0-1--0-0--1', '--0-1-00----1', '1-011-0------', '--011----0--1', '----100--01--', '--0-1----01-1', '1-01-0---01--', '1-0-1----01--', '--011----01--', '1-0---0--01--', '-00110----1--', '--01-000----1', '--0--00--01--', '--0-10---0--1', '1--110-0-01--', '--0110-0----1', '100--000---11', '----1000--1-1', '1-0--00---1-1', '--0-1-0--0---', '10011--00-11-', '1-0---00-0--1', '1---1-00-01--', '--0---00-0-11', '--0--00---111',
         '1-0-10----1-1', '---11-0--01--', '----1-0--01-1', '1-01-00-----1', '1-0--0000---1', '--01--0--01--', '--01--00--1-1', '100---0--0--1', '1-0110----1--', '1-0110-00----', '1-0-1-0-----1', '--0---00-01--', '1--11-00--1-1', '1-0--000--1--', '---110---0111', '--0-1-0---1--', '--0--00-00-1-', '--0-1--0-01--', '---11-00-0--1', '--0---0000--1', '--011--0-0---', '--0--0-0-01-1', '---1-00--01-1', '1--11000----1', '---1100---1-1', '1-0--0---01-1', '--0--000--1-1', '1-01--0---1-1', '1--1-000-01--', '1--11-00-0---', '1-0--0-00011-', '--0-10-0--1-1', '--01-0---01-1', '--0-10-0-0---', '1---10000-11-', '--011--0--1-1', '-00--00-00---', '--0--000-0---', '1-0---0-00--1', '--0-10--0-111', '--0110---0---', '1---100---1-1', '---1100--0---', '1--1--0000111', '1-01---0-01-1', '1-01-0-0-0--1', '---11000--1--', '1--110-000--1', '----100--0--1', '1-01-000-----', '1-0110-0---1-', '1---10-0-01-1', '1-0110------1', '--0110--0-1--', '--0--00-0-1-1', '1-011----0---', '1-011-----1-1', '1---100--0---', '1-0-1---00--1', '----1-000011-', '--0--00--0--1']

# Japon: 208 elementos de 3912
# Tiempo de ejecución: 30.64 minutos
Japon = ['-11-101-1-10-', '0-1----1---01', '011-1----11--', '011-----1----', '-1-1-01-11--1', '-111--11111--', '0-1-------101', '0--11--11110-', '--111---111-1', '-111--1--1101', '--11-01--1-0-', '011----1-11--', '0--1--1--11-1', '0---10111----', '-1111-11-1--1', '0-1---1-----1', '-11-10111--0-', '0-1-----1---1', '01-11-11-110-', '--11-01--11--', '01-1------101', '-1-110--1-101', '-1111-11--101', '-1-1-0-11-101', '011------110-', '-1111-1-111--', '0----011---01', '011---11---0-', '011-1--1-1---', '0-1-1-----1-1', '01--1-111-1-1', '011----1-1-0-', '0--1--1-111--', '01---0-1----1', '0---10--1110-', '0----0111--0-', '-1111-1--11-1', '-1-110-11--01', '-11-10-1-1-01', '---1-01111-01', '-11-101-11---', '-111--1-1110-', '---1-011111-1', '01---01-----1', '-11--01-11-0-', '-11-1011--1-1', '0--11-111-10-', '-11--01111---', '-1-1-0--11-01', '-11--0111-10-', '0-1---1-1----', '--1110-1-1-0-', '01-1--1-1----', '01----111-101', '-1-1-0111---1', '-111----1---1', '0-1-1--11----', '01-1----11---', '011---1--1---', '--11-0--1----', '-111-0----10-', '01-11------01', '01--10------1', '01-1-0-------', '-1-1-0--111-1', '0-11---------', '--1--0-11-101', '-1-1-0-111--1', '0--11-1-11---', '0--11-1--1--1', '011-1-11-----', '-11-10---1101', '01-1---11--0-', '0---101---1-1', '-11--01--11-1', '0---1011----1', '011---1---10-', '01-1---11-1--', '--11-011--10-', '01---011-11--', '--1110-1-11--', '--1-10-11--01', '011-1-1---1--', '-1111-1111---', '0--11-11--1-1', '---1-01-11101', '-1-1-01-1--01', '-111-0-1---0-', '0-1----11--0-', '01--1--111-01', '0--1-0---1---', '0----011--1-1', '--11---111--1', '0-1-1---1--0-', '-1-110-11-1-1', '--1-10--1-101', '01-1-----1--1', '0---10---11-1', '0---10-111---', '-1111-1-11-0-', '--111-1-1--01', '0---101-1-10-', '01-11--1----1', '-11--0-1-1101',
         '01--1-1-11--1', '0----0-1111--', '01---0--11---', '01----1-11-01', '011---------1', '0-1-----1-10-', '-11110-1-----', '---1101-11-01', '01---01-1----', '0--1--11-1--1', '0-1----11-1--', '--111--11-101', '--11--111---1', '-11--0-11110-', '-111-0---1---', '0--1-0-----0-', '01---0--1-1--', '0----0111-1--', '01--10--1----', '-1-1-01-1-1-1', '0--1----1---1', '011---11--1--', '0----0-1-11-1', '-11-10-111-0-', '01--1--1111-1', '0-1--0-------', '0--1-0--1----', '---1101-111-1', '--11--1-11--1', '-11-1011---01', '0--110-------', '0-1-1--1----1', '0--1--1111---', '-11110----1--', '01--1011-1---', '--111-1-1-1-1', '-11--01--1-01', '0----01--1--1', '0-1-1------01', '0--1--1--1-01', '01----1-111-1', '--111011---0-', '-11-101--1--1', '0-1-1---1-1--', '01-11---1-1--', '--11-0------1', '-111-01------', '-1-1101-1---1', '--11----11101', '--11--1-1-101', '-11-10-1-11-1', '01-1---1--1-1', '01---0---1--1', '-111-0-1--1--', '01-1--1-----1', '0----0-1-1-01', '-111--11-1-01', '-11--0--1---1', '01---0--1--0-', '-111--11-11-1', '-11110-----0-', '01---0-11----', '--11-0-1-110-', '-11--01-111--', '--1--01-1---1', '-11-101---101', '0----0--1---1', '-11--011-1--1', '01--1-111--01', '011-1----1-0-', '0-1------1--1', '0-1----1--1-1', '--111011--1--', '01-----111101', '-1-110--11--1', '0---10-1-1--1', '0--1-01------', '-11-10-1111--', '-11-10111-1--', '--1-10-11-1-1', '-11--011--101', '0--1-0-1-----', '0--11--1-11-1', '011-1-1----0-', '-111--1111-0-', '01-11--11----', '0-1-1-11-110-', '01---0-----01', '0--1-0------1', '01-11-----1-1', '0--1-0----1--', '---1101111--1', '01-1---1---01', '--111---11-01', '--11101--1---', '01---0----1-1', '-1111--1-1101', '01--101--110-', '--11-011-1---', '--1--0--11--1', '0----01-11---', '0-1-----11---', '01----1111--1', '-1111-1--1-01']

# USA: 246 elementos de 4526
# Tiempo de ejecución: 36.6 minutos
USA = ['---00---1-1--', '00---11--11--', '0010011----1-', '--1001-0---1-', '00-00-----11-', '001-0--01----', '--10---011-1-', '---0--1-111--', '0--0-1-0-1-1-', '0--0-1-0--1--', '----01--11-1-', '00-0--10--1--', '-01-01-0-1---', '----011-11---', '00---110-1-10', '0---01-0-1---', '----0--011---', '---0----1111-', '001---1011---', '0--00-1---1--', '0--00----11--', '-0--011---11-', '-010-1--11-1-', '-0--0---1-11-', '----0--0-11--', '0---0--0--11-', '0--0---0-11--', '0-10-11---11-', '---00-10-1---', '0------01-11-', '--10-1-01--1-', '0---0-101----', '00---1-0--11-', '-0-0--1-1-11-', '00--01--1--1-', '00-0-11---11-', '---0-1--1-11-', '-0-00--01----', '-0-0-1--1-1--', '---0--10-11--', '00-0--101--1-', '----01-01----', '-----1-01-1--', '---00-101----', '0--0-1-01----', '00---110--1--', '0-10-1--11---', '0--001---1-1-', '00--0-10-1---', '-0-001-0---1-', '0-1001---1---', '00-00-10---1-', '001-0110-----', '--1-0---1-11-', '---0---0-111-', '0--0-1--1-1--', '-----1-0-111-', '-01001---1-1-', '0--0--1-1-11-', '0-10--101--1-', '----01---11--', '00----1011--0', '---00----111-', '---0-110-1-1-', '--1-01--11---', '---001----11-', '--1--11-1-11-', '-0-0-1---111-', '--1001----1--', '0-1--11-11-1-', '-01001--1----', '---0-11-11-1-', '00--0--0--1--', '0-1----01-1--', '---00110---1-', '00--0-1-11---', '--10-1---111-', '00-0----1-11-', '-0-0-1101----', '----0-1-1-11-', '---0-1-0-11--', '-01---101-1--', '-01-0--0--11-', '-01--110--11-', '--100--0-1-1-', '001-01----1--', '0--00--0-1---', '0-100-----11-', '0---0--01--1-', '0-1--1-0--11-', '0-1-0---11-1-', '0010---0--11-', '0---011-1--1-', '001-0----11--', '---0-110--1--', '0--00-10---10', '-01-0-1--11-0', '---0-1-011---', '-01--1-011---', '0010-11-1--1-', '-0-00110-----', '0-1-011-1----', '0----11-1-1--', '0----110--11-', '0--0--1--111-', '-----11011---', '0--001-0-----', '---0011--1-1-', '----0-1--111-', '--1-0-1-1-1--', '0---0-1--11--', '-0-00-1---11-', '0----1--1-11-', '-010-110-1---', '0--0----111--', '-0----1-1111-', '00-----01-1--', '0-----10-11--', '---0-11--11--', '00-00-1--1-1-', '0-10----1-11-', '-0-00----11--', '001-----111--',
       '00---11-11-1-', '00-0--1-11-1-', '001--1-01--1-', '0---0---1-1--', '--10-1101----', '0--001--1----', '00-001---1---', '-01-011-1--1-', '0--00-1-1--1-', '---00--01--1-', '001-01-0---1-', '-0---11-1-11-', '----0--01-1--', '-0-0011--1---', '0--0---011---', '--100--01----', '---00-1-11---', '---0--1011---', '--100----11--', '0---01----11-', '--1-011---11-', '0--0--10--11-', '0---0-10-1-1-', '----0---111--', '--10-1--1-1--', '0-1-0-1-11---', '----0110-1---', '---00--0--1--', '00-----0-111-', '---001--1--1-', '-01-0-10-1-10', '001--1--1-1--', '0-1-0--0--1--', '0--00---11---', '---00-1--11--', '00-0011----10', '-----1--111--', '------101-11-', '0----1-011---', '0---0-10--1--', '-0----10-111-', '0-10--1-1-1--', '0---0----111-', '0-100-10---1-', '0-1-01--1--1-', '00--0---11-1-', '---00----11-0', '0--001----1--', '--10----111--', '----0-10--11-', '0-1--110--1--', '-----1-011-1-', '-0--0-1-1-1--', '-01-0-10--1--', '0--0-110-1---', '-010-1-0--1--', '0-----1-111--', '-0-0---011-1-', '-0--01--11---', '0---0-1-11-1-', '-0-0----111--', '0--0-1---11--', '0---0110---1-', '0--00--01----', '----01-0-1-1-', '-0-0-11-11---', '--1---1-1111-', '0-----101-1--', '00-00-1-1---0', '0----1-0-11--', '--100110-----', '---001--11---', '---0011---1--', '0-1----0-111-', '0----11--111-', '-0-0---0-11--', '---0---01-1--', '0010--10-1-1-', '-010--10--11-', '001----011-1-', '0--0011--1---', '0----1101--1-', '001--110-1-1-', '--1--1-0-11--', '0-------1111-', '00100---1--1-', '---0-1101--1-', '00--011-1----', '001--1101----', '--1-0-101--1-', '00100-1-1----', '0--0-1--11-1-', '---0-1-0--11-', '-------0111--', '----01--1-1--', '001--1---111-', '00-0-1--11---', '0-1-011--1-1-', '001-0--0-1-1-', '0--0-11-11---', '-0---1-0-11--', '-01----01-11-', '-0-00--0-1-1-', '-0--0-1-11-1-', '0010--1--11--', '-0--0-101--1-', '0---01--11---', '-0100---11---', '-0-0-1-01--1-', '00--011--1-1-', '0-100-1--1-10', '---001-0-1---', '0-----1011-1-', '---0-11-1-1--', '00-0--1-1-1--', '---0011-1----', '0---011---1--', '-0-001----1--', '----01-0--1--', '-----110-11--', '0010-1-0-1---', '-0--0-10--1-0', '---00---11-1-']
