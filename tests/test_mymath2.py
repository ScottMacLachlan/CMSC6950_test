import pytest
from mymath import *

@pytest.mark.parametrize("x,x_plus_one",[(0,1),(1,2),(1.5,2.5),(2.25,3.25)])
def test_addone(x,x_plus_one):
    assert addone(x) == x_plus_one

@pytest.mark.parametrize("x,double_x",[(1,2),(0,0),(1.5,3),(2.25,4.5)])
def test_double(x,double_x):
    assert double(x) == double_x

@pytest.mark.parametrize("x,x_plusone_doubled",[(0,2),(1,4),(1.5,5),(2.25,6.5)])
def test_addone_then_double(x,x_plusone_doubled):
    assert addone_then_double(x) == x_plusone_doubled

@pytest.mark.parametrize("x,y,val",[(1,1,0.7080734182735712),(5,0.25,-0.18979332974154567)])
def test_sinc2d_regression(x,y,val):
    assert abs(sinc2d(x,y)-val) < 1e-10