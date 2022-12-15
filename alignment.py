import globall
import fitting
import local
def align(s1, s2, delta, type):
    if type == 'Global': 
        align1, align2, alignCorrds = globall.main(s1, s2, delta)
    elif type == 'Fitting':
        align1, align2, alignCorrds = fitting.fitting(s1, s2, delta)
    elif type == 'Local':
        align1, align2, alignCorrds = local.local(s1, s2, delta)
    return align1, align2, alignCorrds