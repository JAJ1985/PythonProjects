# -*- coding: utf-8 -*-
"""
Created on Tue Nov  5 14:10:58 2019

@author: JOSJOHN
"""

import win32com.client
xlapp = win32com.client.gencache.EnsureDispatch('Excel.Application')
#wb = xlapp.Workbooks.Open('P:\WI\Teams\Programs\J&J CCC\Metrics - Management\Phone CSAT Results.xlsx')
#wb.variant = ('Alta1231!')
wb = xlapp.workbooks.Open('P:\WI\Teams\Programs\J&J CCC\QMS\JOSJOHN\Incentive Build\Incentive Store Reconciliation_TrackingV2.xlsm')
wb.RefreshAll()
xlapp.CalculateUntilAsyncQueriesDone()
xlapp.DisplayAlerts = False
wb.Save()
xlapp.Quit()