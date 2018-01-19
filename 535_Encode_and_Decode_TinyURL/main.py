class Codec:
    
    longUrlTab = {}
    shortUrlTab = {}
    fixedLen = 6

    def encode(self, longUrl):
        """Encodes a URL to a shortened URL.
        
        :type longUrl: str
        :rtype: str
        """
        if (longUrl not in self.longUrlTab):
            newUrl = "http://tinyurl.com/" + "".join(random.choice(string.ascii_lowercase + string.digits) for v in range(self.fixedLen))
            while (newUrl in self.longUrlTab):
                newUrl = "http://tinyurl.com/" + "".join(random.choice(string.ascii_lowercase + string.digits) for v in range(self.fixedLen))
            self.longUrlTab[longUrl] = newUrl
            self.shortUrlTab[newUrl] = longUrl
            return newUrl
        else:
            return self.longUrlTab[longUrl]


    def decode(self, shortUrl):
        """Decodes a shortened URL to its original URL.
        
        :type shortUrl: str
        :rtype: str
        """
        if (shortUrl not in self.shortUrlTab):
            return None
        else:
            return self.shortUrlTab[shortUrl]    
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))
