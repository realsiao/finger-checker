# finger-checker
> Cross-platform network fingerprinting tool

### Usage

**Query the CMS of a specified URL**
```
python3 fig.py -t <TARGET>
```
<img width="1072" alt="image" src="https://user-images.githubusercontent.com/119853210/218536763-91fd5ff9-7b81-4569-9050-8dfb366851d8.png">


**Query the CMS of a specified URL and output the result as a csv file**

```
python3 fig.py -t <TARGET> -m csv -c cms.csv
```
You can choose to output as csv, html, or xml.

<img width="1071" alt="image" src="https://user-images.githubusercontent.com/119853210/218536911-94f1badf-5a96-46ee-bc9f-3f0efbe1bed1.png">

**View help information**

```
python3 fig.py -h
```

<img width="1078" alt="image" src="https://user-images.githubusercontent.com/119853210/218537231-be326fc3-0c85-4d10-a424-522250f268cf.png">

**Enable API**

```
python3 fig.py -A
```
<img width="1073" alt="image" src="https://user-images.githubusercontent.com/119853210/218537389-c6ccca87-a86e-466d-9bb4-47c029f07860.png">

Example:

```
http://127.0.0.1:891/api?query=http://www.mediawiki.org
```
<img width="1111" alt="image" src="https://user-images.githubusercontent.com/119853210/218537758-0cb5dbf9-2ee9-4125-a254-5d37e8969491.png">

By default, the output is in the form of JSON.

You can change the output format to XML:
```
http://127.0.0.1:891/api?query=http://www.mediawiki.org&output=xml
```
<img width="1005" alt="image" src="https://user-images.githubusercontent.com/119853210/218538187-cb2358a4-bb9c-4b40-b327-93f11e6ae62f.png">

### Add more fingerprints

Please add the fingerprint information to the fingerprints.yml file.

<img width="1342" alt="image" src="https://user-images.githubusercontent.com/119853210/218538454-24df329b-63e1-40ed-896e-df290a9fc5af.png">


### MIT License

```
Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```




