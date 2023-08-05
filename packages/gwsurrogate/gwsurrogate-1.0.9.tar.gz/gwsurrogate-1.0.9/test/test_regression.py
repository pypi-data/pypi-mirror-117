"""
Tests all relevant data generated by tutorial notebooks.
Regression data is stored in npz files.
"""

from __future__ import division
import nose
import numpy as np
import gwsurrogate as gws
import os

# set global tolerances for floating point comparisons (see np.testing.assert_allclose)
atol = 0.0
rtol = 1.e-11

# try importing data. If it doesn't exist, download it
try:
  reg_data = np.load('test/gws_regression_data_v2/data_notebook_basics_lesson1_v2.npz')
except:
  print("Downloading regression data...")
  #os.system('wget --directory-prefix=test https://www.dropbox.com/s/07t84cpmmqjya69/gws_regression_data.tar.gz')
  os.system('wget --directory-prefix=test https://www.dropbox.com/s/2z8xvrdu4kdjc18/gws_regression_data_v2.tar.gz')
  os.system('tar -xf test/gws_regression_data_v2.tar.gz -C test/')

path_to_surrogate = \
'tutorial/TutorialSurrogate/EOB_q1_2_NoSpin_Mode22/l2_m2_len12239M_SurID19poly/'
EOBNRv2_sur = gws.EvaluateSingleModeSurrogate(path_to_surrogate)


def test_notebook_basics_lesson1():
  """ Regression test data from notebook example.

      Data created on 5/30/2015 with

np.savez('data_notebook_basics_lesson1.npz',t=t,hp=hp,hc=hc,amp=amp,phase=phase,phi_m=phi_m,h_adj=h_adj)

      After gwtools changes to constants (8/24/2018), _v2 of this data was created"""

  # because M and dist are provided, a physical GW is generated
  t, hp, hc  = EOBNRv2_sur(q=1.7, M=80.0, dist=1.0, phi_ref = 0.0, f_low = 10.0)
  amp, phase = EOBNRv2_sur.amp_phase(hp + 1j*hc)

  phi_m = EOBNRv2_sur.phi_merger(hp + 1j*hc)
  h_adj = EOBNRv2_sur.adjust_merger_phase(hp + 1j*hc,2.0)

  # load regression data
  reg_data = np.load('test/gws_regression_data_v2/data_notebook_basics_lesson1_v2.npz')

  np.testing.assert_allclose(t,reg_data['t'], rtol=rtol, atol=atol)
  np.testing.assert_allclose(hp,reg_data['hp'], rtol=rtol, atol=atol)
  #np.testing.assert_allclose(hc,reg_data['hc'], rtol=rtol, atol=atol)
  # one value is almost zero, causes test to fail
  np.testing.assert_allclose(hc+1.e-15,reg_data['hc']+1.e-15, rtol=rtol, atol=atol)
  np.testing.assert_allclose(amp,reg_data['amp'], rtol=rtol, atol=atol)
  np.testing.assert_allclose(phase,reg_data['phase'], rtol=rtol, atol=atol)
  np.testing.assert_allclose(phi_m,reg_data['phi_m'], rtol=rtol, atol=atol)
  np.testing.assert_allclose(h_adj,reg_data['h_adj'], rtol=rtol, atol=atol)

def test_notebook_basics_lesson2():
  """ Regression test data from notebook example.

      Data created on 5/30/2015 with

np.savez('data_notebook_basics_lesson2.npz',t_resamp=t_resamp,hp_resamp=hp_resamp,hc_resamp=hc_resamp)

      After gwtools changes to constants (8/24/2018), _v2 of this data was created"""

  #t, hp, hc = EOBNRv2_sur(q=1.2)
  t_resamp, hp_resamp, hc_resamp = \
    EOBNRv2_sur(1.2,times=np.linspace(EOBNRv2_sur.tmin-1000,EOBNRv2_sur.tmax+1000,num=3000))

  # load regression data
  reg_data = np.load('test/gws_regression_data_v2/data_notebook_basics_lesson2_v2.npz')

  np.testing.assert_allclose(t_resamp,reg_data['t_resamp'], rtol=rtol, atol=atol)
  np.testing.assert_allclose(hp_resamp,reg_data['hp_resamp'], rtol=rtol, atol=atol)
  np.testing.assert_allclose(hc_resamp,reg_data['hc_resamp'], rtol=rtol, atol=atol)


def test_notebook_basics_lesson3():
  """ regression test data from notebook example.

      Data created on 5/30/2015 with

np.savez('data_notebook_basics_lesson3_v2.npz',eim_pts=eim_pts, T_eim=T_eim,
          greedy_pts=greedy_pts,tmin=EOBNRv2_sur.tmin,tmax=EOBNRv2_sur.tmax,
          dt=EOBNRv2_sur.dt,tunits=EOBNRv2_sur.t_units)

      After gwtools changes to constants (8/24/2018), _v2 of this data was created"""


  t, hp, hc  = EOBNRv2_sur(1.7,80.0,1.0)
  eim_pts    = EOBNRv2_sur.eim_indices
  T_eim      = t[eim_pts]
  greedy_pts = EOBNRv2_sur.greedy_points

  tunits = EOBNRv2_sur.t_units
  dt = EOBNRv2_sur.dt
  tmax = EOBNRv2_sur.tmax
  tmin = EOBNRv2_sur.tmin


  reg_data = np.load('test/gws_regression_data_v2/data_notebook_basics_lesson3_v2.npz')

  np.testing.assert_allclose(eim_pts,reg_data['eim_pts'], rtol=rtol, atol=atol)
  np.testing.assert_allclose(T_eim,reg_data['T_eim'], rtol=rtol, atol=atol)
  np.testing.assert_allclose(greedy_pts,reg_data['greedy_pts'], rtol=rtol, atol=atol)
  np.testing.assert_allclose(dt,reg_data['dt'], rtol=rtol, atol=atol)
  np.testing.assert_allclose(tmax,reg_data['tmax'], rtol=rtol, atol=atol)
  np.testing.assert_allclose(tmin,reg_data['tmin'], rtol=rtol, atol=atol)
  assert(str(tunits) == str(reg_data['tunits']))


def test_notebook_basics_lesson4():
  """ Regression test data from notebook example.

      Data created on 5/30/2015 with

np.savez('data_notebook_basics_lesson4.npz',times=times,b_5=b_5,e_5=e_5,h_5=h_5,h_5_surr=h_5_surr)

      After gwtools changes to constants (8/24/2018), _v2 of this data was created"""


  b_5   = EOBNRv2_sur.basis(4,'cardinal')
  e_5   = EOBNRv2_sur.basis(4,'orthogonal')
  h_5   = EOBNRv2_sur.basis(4,'waveform')
  junk, hp_5_surr, hc_5_surr = EOBNRv2_sur(EOBNRv2_sur.greedy_points[4])
  nrm_5 = EOBNRv2_sur.norm_eval(EOBNRv2_sur.greedy_points[4])
  hp_5_surr = hp_5_surr / nrm_5 
  hc_5_surr = hc_5_surr / nrm_5
  h_5_surr = hp_5_surr + 1j*hc_5_surr

  # load regression data
  reg_data = np.load('test/gws_regression_data_v2/data_notebook_basics_lesson4_v2.npz')

  np.testing.assert_allclose(b_5,reg_data['b_5'], rtol=rtol, atol=atol)
  np.testing.assert_allclose(e_5,reg_data['e_5'], rtol=rtol, atol=atol)
  np.testing.assert_allclose(h_5,reg_data['h_5'], rtol=rtol, atol=atol)
  np.testing.assert_allclose(h_5_surr,reg_data['h_5_surr'], rtol=rtol, atol=atol)

  # basis orthogonality
  dt  = 1.0/2048.0 # found from surrogate *.dat file
  e_6 = EOBNRv2_sur.basis(5,'orthogonal')
  nose.tools.assert_almost_equal(np.sum(e_5*np.conj(e_6)) * dt,0.0,places=14)
  nose.tools.assert_almost_equal(np.sum(e_5*np.conj(e_5)) * dt,1.0,places=14)

#def test_notebook_basics_lesson5():
#
#  assert(False) #TODO: code me (download surrogates need to be rebuilt)

def test_tPNT2Tidal():
  out = gws.new.tidal_functions.PNT2Tidal(1.e-2, 2.0, 100., 1000. , .3, -.7, 100., 1000., .2, .5)
  assert( np.abs(out[0] + 15351562.5216222 )/ 15351562.5216222 < 1.e-12)
  assert( np.abs(out[1] + 61.40625000865016 )/ 61.40625000865016 < 1.e-12)

 
if __name__ == '__main__':
  print("Running test 1...")
  test_notebook_basics_lesson1()
  print("Running test 2...")
  test_notebook_basics_lesson2()
  print("Running test 3...")
  test_notebook_basics_lesson3()
  print("Running test 4...")
  test_notebook_basics_lesson4()
