import discretisedfield as df
def correct_vtk(infile, outfile, scale=1e9):
    """
    Scales the dimenstions of the vtk file by scale. Some programs might have problems 
    with rendering nanoscale surfaces. Scaling the dimensions fixes this problem.
    Usage: 
    correct_vtk(infile, outfile, scale = scale)
    reads the infile scales the dimensions and saves in outfile.
    """
    with open(infile , 'r') as f:
        vtk_string = f.read()
    coordinate_lines = [6 , 8, 10]
    string_list = vtk_string.split('\n')
    for i in coordinate_lines:
        corrected_list = [str(float(x)*scale) for x in string_list[i].split(' ') ]
        string_list[i] = ' '.join(corrected_list)
    with open(outfile, 'w') as f: 
        f.write('\n'.join(string_list))

def sub_sample(field_read, spec ):
    xstart=spec['xstart']
    xend = spec['xend']
    ystart = spec['ystart']
    yend = spec['yend']
    zstart =spec['zstart']
    zend = spec['zend']
    xmeshsize = spec['xmeshsize']
    ymeshsize = spec['ymeshsize']
    zmeshsize = spec['zmeshsize']
    dim = spec['dim']
    region = df.Region(p1=(xstart, ystart, zstart), p2=(xend, yend, zend))
    mesh = df.Mesh(region=region, n=(int((xend-xstart)/xmeshsize), int((yend-ystart)/ymeshsize), int((zend-zstart)/zmeshsize)))
    f1 = df.Field(mesh, dim=dim, value=field_read)
    return f1
    