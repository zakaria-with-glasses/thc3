from io import BufferedReader

class Engine:

    def LoadFile2Hash(self, filepath:str) -> int:
        with open(filepath, "rb") as f:
            csum = self.CollectionBucket(f)
            print(csum)
            return csum



    def CollectionBucket(self, input_:str|BufferedReader) -> int:
        """self.CollectionBucket method splits between a simple
        string hash or a filetype hash."""

        if type(input_) is str:
            if len(input_) > 16:
                return self.LongInputCollector([input_[i:i+16] for i in range(0, len(input_), 16)])
        
            return self.LongInputCollector(input_)
        elif type(input_) is BufferedReader:
            l = []
            while True:
                chunk = input_.read(1024)
                l.append(chunk)
                if not chunk:
                    break


            return self.LongInputCollector([l[i:i+16] for i in range(0, len(l), 16)])
        
    def LongInputCollector(self, long_input:str|list) -> int:
        """self.LongInputCollector method collectes chunked 
        input to pump it into the hash function"""

        if type(long_input) is list:
            collection = []
            start_value = 0
            for j in long_input[0]:        # each element in array
                collection.append(self.HashFunction(j))
            for k in collection:
                start_value ^= k

            return start_value          #xor of each hash iteration to prevent reversing the function

        elif type(long_input) is str:
            return self.HashFunction(long_input)
        

    
    def HashFunction(self, chunk:bytes|str) -> int:
        """self.HashFunction method pumps a
        '16 byte' chunk into the hash function."""
        hashresult = len(chunk)
        if type(chunk) is str:
            if len(chunk) <= 16:
                padding = "*"*(16-len(chunk))
                chunk+=padding

            for i in range(0, len(chunk)):
                hashresult += ord(chunk[i])**(i%13)

            return hashresult
        
        elif type(chunk) is bytes:
            if len(chunk) <= 16:
                padding = b"\x99"*(16-len(chunk))
                chunk+=padding

            for i in range(0, len(chunk)):
                hashresult += chunk[i]**(i%13)
            
            return hashresult
        
csum = Engine()
csum.LoadFile2Hash("hello.txt")