from media import Media

class TestMedia(object):
    
    def test_calc(self):
        result = Media.media(5, 5)
        assert result == 5
    
    def test_calc2(self):
        result = Media.media(40, 50)
        assert result == 45
    
    def test_calc3(self):
        result = Media.media(36, 64)
        assert result == 50
    
    def test_calc4(self):
        result = Media.media(10, 50)
        assert result == 30
    
    def test_calc5(self):
        result = Media.media(36, 20)
        assert result == 28