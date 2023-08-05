double ipow(double base, long exponent);
static PyObject *eval_fit(PyObject *self, PyObject *args);
static PyObject *normalize_y(PyObject *self, PyObject *args);
static PyObject *get_ds_fit_x(PyObject *self, PyObject *args);
static PyObject *assemble_dydt(PyObject *self, PyObject *args);
static PyObject *ab4_dy(PyObject *self, PyObject *args);
static PyObject *binom(PyObject *self, PyObject *args);
static PyObject *wigner_coef(PyObject *self, PyObject *args);
double factorial(int n);
double factorial_ratio(int n, int k);
double _binomial(int n, int k);
double _wigner_coef(int ell, int mp, int m);
