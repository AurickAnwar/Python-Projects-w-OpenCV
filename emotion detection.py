from exceedCv import google_CV as cv

j_path = "vision-project-207707-f84d39ceed76.json"

cv.google_auth(j_path)

path = "angry.jpg"

likelihood_name = ('UNKNOWN', 'VERY UNLIKELY', 'UNLIKELY', 'POSSIBLE', 'LIKELY', 'VERY LIKELY')

faces, refPt = cv.detect_faces(path, max_results= 10)

cv.display_allborders(refPt, path)

emotions, face_box = cv.display_emotion(faces)

for e in emotions:
    angry, joy, sor, surp = e
    print('angry: {}', likelihood_name[angry])
    print('happy: {}', likelihood_name[joy])
    print('sad: {}', likelihood_name[sor])
    print('surprised: {}', likelihood_name[surp])
