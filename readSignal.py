import wfdb

dbName = 'wrist'
recName = 's1_walk'

# Read part of a record from Physiobank
sig, fields = wfdb.rdsamp(dbName+'/'+recName, sampfrom=1000, channels=[0])
record = wfdb.rdrecord(dbName+'/'+recName)
print(record.__dict__)
# Call the gateway wrsamp function, manually inserting fields as function input parameters
wfdb.wrsamp('ecg-record', fs=256, units=['mV'], sig_name=['chest_ecg'], p_signal=sig, fmt=['16'])

# The new file can be read
record = wfdb.rdrecord('ecg-record')

wfdb.plot_wfdb(record)
