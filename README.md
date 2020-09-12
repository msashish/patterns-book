### Step0   Create virtual environment
        python3 -m venv patterns-book-venv
        source patterns-book-venv/bin/activate
        
### Step1   Create all code in below order and Makefile
        test_batches.py   then model.py
        test_allocate.py  then edit model.py
        conftest.py and orm.py then test_orm.py
        test_repository.py and then repository.py 
        
### Step2   Write tests/unit/test_batches.py and src/model.py
        Use -s option if you want to display messages
        
        pytest tests/unit  -s    (pytest --tb=short -s)
        pytest tests/unit/test_batches.py  -s
        pytest tests/unit/test_allocate.py  -s
        pytest tests/unit/test_orm.py  -s
        pytest tests/unit/test_repository.py  -s
        pytest tests/unit/test_value_objects.py  -s 
        
  
