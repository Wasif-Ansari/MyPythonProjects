
def scan_resume(resume):
    import spacy
    
    import en_core_web_sm
    # nlp = en_core_web_sm.load()
    nlp = spacy.load('en_core_web_sm_mirror') 
    from resume_parser import resumeparse
    data = resumeparse.read_file(resume)
    for i,j in data.items():
        print(f"{i}:>>{j}")

scan_resume("Wasif Ansari Resume.pdf")