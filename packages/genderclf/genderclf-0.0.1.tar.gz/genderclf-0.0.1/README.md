## GenderClassifier Tool
+ For classifying gender of individuals using their first names

### Installation
```bash
pip install genderclf
```

### Usage
#### Basic usage
```python
>>> from genderclf import GenderClassifier
>>> g = GenderClassifier()
>>> g.name = 'Hemant'
>>> g.predict()
```

#### Loading Different Models
```python
>>> from genderclf import GenderClassifier
>>> g = GenderClassifier()
>>> g.name = 'Hansa'
>>> g.load('logit')
>>> g.predict()
```

#### Using the Classify Method
```python
>>> from genderclf import GenderClassifier
>>> g = GenderClassifier()
>>> g.load('nb')
>>> g.classify("Hemant")
```

#### Check Gender
```python
>>> from genderclf import GenderClassifier
>>> g = GenderClassifier()
>>> g.is_male("Hemant")
```

```python
>>> from genderclf import GenderClassifier
>>> g = GenderClassifier()
>>> g.is_female("Hansa")
```

#### Requirements
+ Joblib
+ Scikit-learn

#### Maintainer
+ Ankit Hemant Lade(ankitlade12@gmail.com)
