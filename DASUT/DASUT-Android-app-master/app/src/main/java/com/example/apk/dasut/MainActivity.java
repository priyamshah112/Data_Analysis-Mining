package com.example.apk.dasut;

import android.*;
import android.Manifest;
import android.accounts.Account;
import android.accounts.AccountManager;
import android.content.Context;
import android.content.Intent;
import android.content.IntentSender;
import android.content.pm.ApplicationInfo;
import android.content.pm.PackageInfo;
import android.content.pm.PackageManager;
import android.database.Cursor;
import android.location.Location;
import android.net.Uri;
import android.net.wifi.WifiInfo;
import android.net.wifi.WifiManager;
import android.os.AsyncTask;
import android.os.Build;
import android.os.Bundle;
import android.os.StrictMode;
import android.provider.MediaStore;
import android.provider.Settings;
import android.support.annotation.NonNull;
import android.support.annotation.Nullable;
import android.support.v4.app.ActivityCompat;
import android.support.v4.content.ContextCompat;
import android.support.v7.app.AppCompatActivity;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.CheckBox;
import android.widget.TextView;
import android.widget.Toast;

import com.google.android.gms.common.ConnectionResult;
import com.google.android.gms.common.api.GoogleApiClient;
import com.google.android.gms.common.api.PendingResult;
import com.google.android.gms.common.api.ResultCallback;
import com.google.android.gms.common.api.Status;
import com.google.android.gms.location.FusedLocationProviderApi;
import com.google.android.gms.location.LocationRequest;
import com.google.android.gms.location.LocationServices;
import com.google.android.gms.location.LocationSettingsRequest;
import com.google.android.gms.location.LocationSettingsResult;
import com.google.android.gms.location.LocationSettingsStatusCodes;
import com.google.firebase.database.DatabaseReference;
import com.google.firebase.database.FirebaseDatabase;

import org.jetbrains.annotations.NotNull;

import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.List;

import static android.os.Build.MANUFACTURER;

public class MainActivity extends AppCompatActivity implements GoogleApiClient.ConnectionCallbacks, GoogleApiClient.OnConnectionFailedListener, com.google.android.gms.location.LocationListener
    {
        private TextView email, apps, loc2, device2, androidid2, wifi2, songstv;
        private Button pusher ;
        private static String ip_ = "192.168.1.106";
        private static String port_ = ":8080";
        private GoogleApiClient googleApiClient;
        private LocationRequest locationRequest;
        private FusedLocationProviderApi locationProvider = LocationServices.FusedLocationApi;
        public Double myLongitude1 = 0.0;
        public Double myLatitude1 = 0.0;
        public String accountName = "";
        public String MODEL ;
        public String ID ;
        public String currentDateandTime ;
        public String android_id ;
        public StringBuilder builder ;
        private static final int PERMISSIONS_REQUEST = 133; //This could be any number, used to request permissions
        private static final int REQUEST_CHECK_SETTINGS = 156;
        private static final String TAG = "MainActivity";
        public boolean apimmFlag = false;
        private int linkSpeed;
        private String[] permissions = {android.Manifest.permission.ACCESS_FINE_LOCATION, android.Manifest.permission.ACCESS_COARSE_LOCATION, android.Manifest.permission.GET_ACCOUNTS, android.Manifest.permission.READ_EXTERNAL_STORAGE};
        DatabaseReference firebasedata;
        CheckBox send_check;


        @Override
        protected void onCreate(Bundle savedInstanceState) {
            super.onCreate(savedInstanceState);
            setContentView(R.layout.activity_main);
            Context context = this;
            email = (TextView) findViewById(R.id.email2);
           // apps = (TextView) findViewById(R.id.apps2);
            device2  = (TextView) findViewById(R.id.device2);
           // androidid2 = (TextView) findViewById(R.id.androidid2);
           // wifi2 = (TextView) findViewById(R.id.wifi2);
            pusher = (Button) findViewById(R.id.push);
            android_id = Settings.Secure.getString(this.getContentResolver(), Settings.Secure.ANDROID_ID);
            SimpleDateFormat sdf = new SimpleDateFormat("ddMMyyyy_HHmmss");
            currentDateandTime = sdf.format(new Date());
            firebasedata = FirebaseDatabase.getInstance().getReference("user_data");
            send_check = (CheckBox) findViewById(R.id.send_data);
            //Toast.makeText(getApplicationContext(), "Please hit the send button", Toast.LENGTH_LONG).show();
            pusher.setOnClickListener(new View.OnClickListener() {
                @Override
                public void onClick(View view) {
                    // Pushing data up there
                    Intent i = new Intent(getApplicationContext(), TimeService.class);
                    i.putExtra("send_data",String.valueOf(send_check.isChecked()));
                    startService(i);
                    pushOnFirebase();
                }
            });

            if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.M) {
                //Note: The code below requests each permission individually
                /* Toast.makeText(this,"SDk >  23", Toast.LENGTH_LONG).show();
                if (ContextCompat.checkSelfPermission(context, android.Manifest.permission.GET_ACCOUNTS) != PackageManager.PERMISSION_GRANTED) {
                    // Should we show an explanation?
                    if (ActivityCompat.shouldShowRequestPermissionRationale(this, android.Manifest.permission.GET_ACCOUNTS)) {
                    } else {
                        // No explanation needed, we can request the permission.
                        ActivityCompat.requestPermissions(this, new String[]{android.Manifest.permission.GET_ACCOUNTS}, PERMISSIONS_REQUEST_GET_ACCOUNTS);
                        // MY_PERMISSIONS_REQUEST_GET_ACCOUNTS is an app-defined int constant. The callback method gets the result of the request.
                    }
                }

                if (ContextCompat.checkSelfPermission(context, Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
                    // Should we show an explanation?
                    if (ActivityCompat.shouldShowRequestPermissionRationale(this, android.Manifest.permission.GET_ACCOUNTS)) {
                    } else {
                        // No explanation needed, we can request the permission.
                        ActivityCompat.requestPermissions(this, new String[]{android.Manifest.permission.ACCESS_FINE_LOCATION}, PERMISSIONS_REQUEST_GET_LOCATION);
                        // MY_PERMISSIONS_REQUEST_GET_ACCOUNTS is an app-defined int constant. The callback method gets the result of the request.
                    }
                }*/
                //Request multiple permissions simulataneously
                ActivityCompat.requestPermissions(this, permissions, PERMISSIONS_REQUEST);
            }
            //Toast.makeText(getApplicationContext(), "Please hit the send button", Toast.LENGTH_LONG).show();
            /*
            if (Build.VERSION.SDK_INT < 23)
            {
                apimmFlag = false ;
            }
            else
            {
                apimmFlag = true ;
            }
            */

            // ************DO NOT TOUCH THIS*****************
            receive(android_id);
            // ************DO NOT TOUCH THIS*****************



            // Setting values and displaying on textviews
            // ---------------------------------------------------------------

            // Extracting system information
            MODEL = android.os.Build.MODEL;
            ID = android.os.Build.ID;



            // Setting the Android Device ID
            // *******************androidid2.setText(android_id+"\n");

            // Setting the Device and Manufacturer details
            // *******************device2.setText(MANUFACTURER+" "+MODEL+" (Android "+androidOS+")\n");

            if(Build.VERSION.SDK_INT < Build.VERSION_CODES.M) {
                if (ContextCompat.checkSelfPermission(context, android.Manifest.permission.GET_ACCOUNTS) == PackageManager.PERMISSION_GRANTED) {
                    // Extracting user (Google) account details
                    Account accounts[] = getAccount(AccountManager.get(getApplicationContext()));
                    for (Account account : accounts) {
                        accountName += account.name + "|";
                        String fullName = accountName.substring(0, accountName.lastIndexOf("@"));
                        // permission was granted, yay! Do the
                        // contacts-related task you need to do.
                    }
                    // *******************email.setText(accountName);
                }
            }
            //if (apimmFlag == false)
            //{
                // Extracting user (Google) account details
                /*Account account = getAccount(AccountManager.get(context));
                accountName += account.name;
                String fullName = accountName.substring(0, accountName.lastIndexOf("@"));
                email.setText(accountName+"\n");*/
            //}

            // For extracting non-system applications
            List<PackageInfo> applist = getPackageManager().getInstalledPackages(0);
            builder = new StringBuilder();
            int i = 1;
            for (PackageInfo details : applist) {

                if ((details.applicationInfo.flags & ApplicationInfo.FLAG_SYSTEM) == 0) {
                    //String pack = details.packageName;
                    if (Build.VERSION.SDK_INT >= 9) {
                        SimpleDateFormat dateFormat = new SimpleDateFormat("ddMMyyyy_HHmmss");

                        String installTime = dateFormat.format( new Date( details.firstInstallTime ) );
                        Log.d(TAG, "Installed: " + installTime);

                        String updateTime = dateFormat.format( new Date( details.lastUpdateTime ) );
                        Log.d(TAG, "Updated: " + updateTime);
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
            // *******************apps.setText(builder.toString());

            // WiFi
            WifiManager wifiManager = (WifiManager) getApplicationContext().getSystemService(Context.WIFI_SERVICE);
            WifiInfo wifiInfo = wifiManager.getConnectionInfo();
            if (wifiInfo != null) {
                 linkSpeed = wifiInfo.getLinkSpeed(); //measured using WifiInfo.LINK_SPEED_UNITS
                // *******************wifi2.setText("Speed: "+linkSpeed+" Megabits per second\n");

            }

            // Location

            //if (apimmFlag == false)
            //{
               // loc2 = (TextView) findViewById(R.id.loc2);
                googleApiClient = new GoogleApiClient.Builder(this)
                        .addApi(LocationServices.API)
                        .addConnectionCallbacks(this)
                        .addOnConnectionFailedListener(this).build();

                locationRequest = new LocationRequest();
                locationRequest.setInterval(10 * 1000); // save battery by checking every 10 seconds
                locationRequest.setFastestInterval(15 * 1000);
                locationRequest.setPriority(LocationRequest.PRIORITY_BALANCED_POWER_ACCURACY);
            //}

            // ---------------------------------------------------------------


        }

        @Override
        public void onRequestPermissionsResult(int requestCode, @NotNull String permissions[], @NotNull int[] grantResults) {
            switch (requestCode) {
                case PERMISSIONS_REQUEST: {
                    // If request is cancelled, the result arrays are empty.
                    if (grantResults.length > 0 && grantResults[2] == PackageManager.PERMISSION_GRANTED) {
                        Account accounts[] = getAccount(AccountManager.get(getApplicationContext()));
                        for (Account account : accounts) {
                            accountName += account.name + "|";
                            String fullName = accountName.substring(0, accountName.lastIndexOf("@"));
                            // permission was granted, yay! Do the
                            // contacts-related task you need to do.
                        }
                        // ******************* email.setText(accountName);
                    } //else accountName = "Cannot access account details";
                    if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED && grantResults[1] == PackageManager.PERMISSION_GRANTED) {
                        LocationSettingsRequest.Builder builder = new LocationSettingsRequest.Builder().addLocationRequest(locationRequest);
                        builder.setAlwaysShow(true);

                        PendingResult<LocationSettingsResult> result = LocationServices.SettingsApi.checkLocationSettings(googleApiClient, builder.build());
                        result.setResultCallback(new ResultCallback<LocationSettingsResult>() {
                            @Override
                            public void onResult(LocationSettingsResult result) {
                                final Status status = result.getStatus();
                                switch (status.getStatusCode()) {
                                    case LocationSettingsStatusCodes.SUCCESS:
                                        Log.i(TAG, "All location settings are satisfied.");
                                        break;
                                    case LocationSettingsStatusCodes.RESOLUTION_REQUIRED:
                                        Log.i(TAG, "Location settings are not satisfied. Show the user a dialog to upgrade location settings ");

                                        try {
                                            // Show the dialog by calling startResolutionForResult(), and check the result
                                            // in onActivityResult().
                                            status.startResolutionForResult(MainActivity.this, REQUEST_CHECK_SETTINGS);
                                        } catch (IntentSender.SendIntentException e) {
                                            Log.i(TAG, "PendingIntent unable to execute request.");
                                        }
                                        break;
                                    case LocationSettingsStatusCodes.SETTINGS_CHANGE_UNAVAILABLE:
                                        Log.i(TAG, "Location settings are inadequate, and cannot be fixed here. Dialog not created.");
                                        break;
                                }
                            }
                        });
                    }
                    /*
                    if (grantResults.length > 0 && grantResults[3] == PackageManager.PERMISSION_GRANTED) {
                        Uri uri = MediaStore.Audio.Media.EXTERNAL_CONTENT_URI;
                        String selection = MediaStore.Audio.Media.IS_MUSIC + "!=0";
                        Cursor cursor = getContentResolver().query(uri, null, selection, null, null);
                        String song ="";
                        if (cursor != null) {
                            if (cursor.moveToFirst()) {
                                do {
                                    String name = cursor.getString(cursor.getColumnIndex(MediaStore.Audio.Media.DISPLAY_NAME));
                                    String artist = cursor.getString(cursor.getColumnIndex(MediaStore.Audio.Media.ARTIST));
                                    String url = cursor.getString(cursor.getColumnIndex(MediaStore.Audio.Media.DATA));
                                    String title = cursor.getString(cursor.getColumnIndex(MediaStore.Audio.Media.TITLE));
                                    String duration = cursor.getString(cursor.getColumnIndex(MediaStore.Audio.Media.DURATION));
                                    //SongInfo s = new SongInfo(name, artist, url);
                                    //_songs.add(s);
                                    song += title+" "+artist+" "+" "+duration+"\n";

                                } while (cursor.moveToNext());

                            }

                            cursor.close(); }
                        songstv = (TextView) findViewById(R.id.songs);
                        songstv.setText(song);
                    }*/
                }
                    //if (grantResults.length > 0 && grantResults[0] == PackageManager.PERMISSION_GRANTED) {
                    //  requestLocationUpdates();
                    //}
                }

                // other 'case' lines to check for other
                // permissions this app might request
        }


        public void pushOnFirebase()
        {
            //if (apimmFlag == false)
            //{
                UserData userData = new UserData(android_id, currentDateandTime,  MODEL, ID, MANUFACTURER, Build.VERSION.RELEASE, accountName, builder.toString(), String.valueOf(linkSpeed), myLongitude1, myLatitude1, "None", String.valueOf(send_check.isChecked()));
                String id = firebasedata.push().getKey();
                firebasedata.push().setValue(userData);
                Toast.makeText(MainActivity.this, "Data uploaded!", Toast.LENGTH_LONG).show();
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

        // Method to get account name
        public static Account[] getAccount(AccountManager accountManager) {
            Account[] accounts = accountManager.getAccountsByType("com.google");
            /*Account account;
            if (accounts.length > 0) {
                account = accounts[0];
            } else {
                account = null;
            }*/
            return accounts;
        }

        public static void getInternet() {
            StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
            StrictMode.setThreadPolicy(policy);
        }

        public static String readKernelVersion() {
            try {
                Process p = Runtime.getRuntime().exec("uname -a");
                InputStream is = null;
                if (p.waitFor() == 0) {
                    is = p.getInputStream();
                } else {
                    is = p.getErrorStream();
                }
                BufferedReader br = new BufferedReader(new InputStreamReader(is), 1024);
                String line = br.readLine();
                br.close();
                return line;
            } catch (Exception ex) {
                return "ERROR: " + ex.getMessage();
            }
        }


        public static String getDeviceModelNumber() {
            String manufacturer = Build.VERSION.CODENAME;
            String model = Build.MODEL;
            if (model.startsWith(manufacturer)) {
                return capitalize(model);
            } else {
                return capitalize(manufacturer) + " " + model;
            }
        }

        private static String capitalize(String s) {
            if (s == null || s.length() == 0) {
                return "";
            }
            char first = s.charAt(0);
            if (Character.isUpperCase(first)) {
                return s;
            } else {
                return Character.toUpperCase(first) + s.substring(1);
            }
        }

        // -------------------------------------------------------------------------------------
        // HTTP POST DATA


        public void receive(String info_text) {

            DroneTest req = new DroneTest();
            //Toast.makeText(getApplicationContext(), info_text, Toast.LENGTH_SHORT).show();
            req.execute(info_text);
        }

        @Override
        public void onConnected(@Nullable Bundle bundle) {
            requestLocationUpdates();
        }

        private void requestLocationUpdates() {
            if (ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
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
            myLatitude1 = location.getLatitude();
            myLongitude1 = location.getLongitude();
            // *******************loc2.setText("Latitude : " + String.valueOf(myLatitude1)+"\nLongitude : " + String.valueOf(myLongitude1));
        }

        @Override
        protected void onStart() {
            super.onStart();
            //if (apimmFlag == false)
                googleApiClient.connect();
        }

        @Override
        protected void onResume() {
            super.onResume();
            //if (apimmFlag == false)
            //{
                if (googleApiClient.isConnected()) {
                    requestLocationUpdates();
               // }
            }
        }

        @Override
        protected void onPause() {
            super.onPause();
           // if (apimmFlag == false)
            //{
                //LocationServices.FusedLocationApi.removeLocationUpdates(googleApiClient, this);
            //}
        }

        @Override
        protected void onStop() {
            super.onStop();
            //if (apimmFlag)
            //{
                googleApiClient.disconnect();
            //}
        }


        public class DroneTest extends AsyncTask<String, Integer, String> {
            @Override
            protected void onPreExecute() {
            }

            @Override
            protected String doInBackground(String... params) {
                // TODO Auto-generated method stub
                // Call your web service here
                String android_id =Settings.Secure.getString(getContentResolver(),Settings.Secure.ANDROID_ID);
                String targetURL = "http://"+ip_+port_+"/" ;
                String urlParameters = android_id ;

                // Getting data
                String OSNAME = System.getProperty("os.name");
                HttpURLConnection connection = null;
                try {
                    //Create connection

                    URL url = new URL(targetURL);
                    connection = (HttpURLConnection) url.openConnection();
                    connection.setRequestMethod("POST");
                    connection.setRequestProperty("Content-Type",
                            "application/x-www-form-urlencoded");

                    connection.setRequestProperty("Content-Length",
                            Integer.toString(urlParameters.getBytes().length));
                    connection.setRequestProperty("Content-Language", "en-US");

                    connection.setUseCaches(false);
                    connection.setDoOutput(true);

                    //Send request
                    DataOutputStream wr = new DataOutputStream (
                            connection.getOutputStream());
                    wr.writeBytes(urlParameters);
                    //wr.writeBytes(OSNAME);
                    wr.close();

                    //Get Response
                    InputStream is = connection.getInputStream();
                    BufferedReader rd = new BufferedReader(new InputStreamReader(is));
                    StringBuilder response = new StringBuilder(); // or StringBuffer if Java version 5+
                    String line;
                    while ((line = rd.readLine()) != null) {
                        response.append(line);
                        response.append('\r');
                    }
                    rd.close();
                    Toast.makeText(getApplicationContext(),"Connection success!",Toast.LENGTH_LONG).show();

                    return response.toString();
                } catch (Exception e) {
                    e.printStackTrace();
                    return null;
                } finally {
                    if (connection != null) {
                        connection.disconnect();
                    }
                }
            }

            @Override
            protected void onPostExecute(String result) {
                // TODO Auto-generated method stub
                // Update your UI here
               // Toast.makeText(getApplicationContext(),"Howdy!",Toast.LENGTH_SHORT).show();
                return;
            }
        }

    // -------------------------------------------------------------------------------------
    }




//package com.example.apk.dasut;
//
//import android.Manifest;
//import android.accounts.Account;
//import android.accounts.AccountManager;
//import android.content.Context;
//import android.content.pm.ApplicationInfo;
//import android.content.pm.PackageInfo;
//import android.content.pm.PackageManager;
//import android.location.Location;
//import android.net.wifi.WifiInfo;
//import android.net.wifi.WifiManager;
//import android.os.AsyncTask;
//import android.os.Build;
//import android.os.Bundle;
//import android.os.StrictMode;
//import android.provider.Settings;
//import android.support.annotation.NonNull;
//import android.support.annotation.Nullable;
//import android.support.v4.app.ActivityCompat;
//import android.support.v4.content.ContextCompat;
//import android.support.v7.app.AppCompatActivity;
//import android.widget.TextView;
//import android.widget.Toast;
//
//import com.google.android.gms.common.ConnectionResult;
//import com.google.android.gms.common.api.GoogleApiClient;
//import com.google.android.gms.location.FusedLocationProviderApi;
//import com.google.android.gms.location.LocationRequest;
//import com.google.android.gms.location.LocationServices;
//
//import java.io.BufferedReader;
//import java.io.DataOutputStream;
//import java.io.InputStream;
//import java.io.InputStreamReader;
//import java.net.HttpURLConnection;
//import java.net.URL;
//import java.util.List;
//
//public class MainActivity extends AppCompatActivity implements GoogleApiClient.ConnectionCallbacks, GoogleApiClient.OnConnectionFailedListener, com.google.android.gms.location.LocationListener {
//
//    private TextView loc2;
//
//    static final Integer ACCOUNTS = 123;
//    static final Integer LOC = 456;
//
//    // For location
//    private GoogleApiClient googleApiClient;
//    private LocationRequest locationRequest;
//    private FusedLocationProviderApi locationProvider = LocationServices.FusedLocationApi;
//
//    private static final int MY_PERMISSIONS_REQUEST_CODE = 1;
//
//    @Override
//    protected void onCreate(Bundle savedInstanceState) {
//        super.onCreate(savedInstanceState);
//        setContentView(R.layout.activity_main);
//
//        Context context = this;
//
//        if (Build.VERSION.SDK_INT < 23)
//        {
//            maal();
//        }
//        else
//        {
//            if (checkPermission())
//            {
//                Toast.makeText(getApplicationContext(), "All permissions granted!", Toast.LENGTH_LONG).show();
//            }
//            else
//            {
//                requestPermission();
//            }
//        }
//
//    }
//
//    public void requestPermission()
//    {
//        ActivityCompat.requestPermissions(MainActivity.this, new String[] {android.Manifest.permission.ACCESS_FINE_LOCATION, Manifest.permission.GET_ACCOUNTS}, MY_PERMISSIONS_REQUEST_CODE);
//    }
//
//    @Override
//    public void onRequestPermissionsResult(int requestCode, @NonNull String permissions[], @NonNull int[] grantResults)
//    {
//        switch(requestCode)
//        {
//            case MY_PERMISSIONS_REQUEST_CODE:
//                if (0 < grantResults.length)
//                {
//                    boolean locPermission;
//                    if (grantResults[0] == PackageManager.PERMISSION_GRANTED) locPermission = true;
//                    else locPermission = false;
//
//                    boolean accountsPermission;
//                    if (grantResults[1] == PackageManager.PERMISSION_GRANTED)
//                        accountsPermission = true;
//                    else accountsPermission = false;
//
//                    if (locPermission && accountsPermission)
//                    {
//                        maal();
//
//
//
//                        loc2 = (TextView) findViewById(R.id.loc2);
//                        googleApiClient = new GoogleApiClient.Builder(this)
//                                .addApi(LocationServices.API)
//                                .addConnectionCallbacks(this)
//                                .addOnConnectionFailedListener(this).build();
//
//                        locationRequest = new LocationRequest();
//                        locationRequest.setInterval(10 * 1000); // save battery by checking every 10 seconds
//                        locationRequest.setFastestInterval(15 * 1000);
//                        locationRequest.setPriority(LocationRequest.PRIORITY_BALANCED_POWER_ACCURACY);
//                    }
//
//                    else
//                    {
//                        Toast.makeText(this, "MISERABLE BITCH! GRANT THE PERMISSIONS!",Toast.LENGTH_LONG).show();
//                    }
//                }
//                break;
//        }
//    }
//
//    public boolean checkPermission()
//    {
//        int locPermission = ContextCompat.checkSelfPermission(getApplicationContext(), Manifest.permission.ACCESS_FINE_LOCATION);
//        int accountsPermission = ContextCompat.checkSelfPermission(getApplicationContext(), Manifest.permission.GET_ACCOUNTS);
//
//        return locPermission == PackageManager.PERMISSION_GRANTED && accountsPermission == PackageManager.PERMISSION_GRANTED;
//
//    }
//
//
//
//    public void maal()
//    {
//        GoogleApiClient googleApiClient;
//        LocationRequest locationRequest;
//        FusedLocationProviderApi locationProvider = LocationServices.FusedLocationApi;
//        Double myLongitude ;
//        Double myLatitude ;
//
//        Context context = MainActivity.this;
//
//        String android_id = Settings.Secure.getString(this.getContentResolver(), Settings.Secure.ANDROID_ID);
//
//        TextView email = (TextView) findViewById(R.id.email2);
//        TextView apps = (TextView) findViewById(R.id.apps2);
//        TextView device2 = (TextView) findViewById(R.id.device2);
//        TextView androidid2 = (TextView) findViewById(R.id.androidid2);
//        TextView wifi2 = (TextView) findViewById(R.id.wifi2);
//
////        Toast.makeText(this, "Please enable location services!", Toast.LENGTH_LONG).show();
////        Intent intent = new Intent(Settings.ACTION_LOCATION_SOURCE_SETTINGS);
////        startActivity(intent);
//
//        // ************DO NOT TOUCH THIS*****************
//        receive(android_id);
//        // ************DO NOT TOUCH THIS*****************
//
//
//        // Setting values and displaying on textviews
//        // ---------------------------------------------------------------
//
//        // Extracting system information
//        String MODEL = android.os.Build.MODEL;
//        String ID = android.os.Build.ID;
//        String MANUFACTURER = android.os.Build.MANUFACTURER;
//        String androidOS = Build.VERSION.RELEASE;
//
//        // Setting the Android Device ID
//        androidid2.setText(ID+"\n");
//
//        // Setting the Device and Manufacturer details
//        device2.setText(MANUFACTURER+" "+MODEL+" (Android "+androidOS+")\n");
//
//        // Extracting user (Google) account details
//        Account account = getAccount(AccountManager.get(context));
//        String accountName = account.name;
//        String fullName = accountName.substring(0, accountName.lastIndexOf("@"));
//        email.setText(accountName+"\n");
//
//        // For extracting non-system applications
//        List<PackageInfo> applist = getPackageManager().getInstalledPackages(0);
//        StringBuilder builder = new StringBuilder();
//        int i = 1;
//        for (PackageInfo details : applist) {
//
//            if ((details.applicationInfo.flags & ApplicationInfo.FLAG_SYSTEM) == 0) {
//                // if full package name is to be printed, simply append 'details'
//                builder.append(i+". "+details.applicationInfo.loadLabel(getPackageManager()).toString() + " - v" + details.versionCode + "\n");
//                i++ ;
//            }
//        }
//        apps.setText(builder.toString());
//
//        // WiFi
//        WifiManager wifiManager = (WifiManager) getApplicationContext().getSystemService(Context.WIFI_SERVICE);
//        WifiInfo wifiInfo = wifiManager.getConnectionInfo();
//        if (wifiInfo != null) {
//            Integer linkSpeed = wifiInfo.getLinkSpeed(); //measured using WifiInfo.LINK_SPEED_UNITS
//            wifi2.setText("Speed: "+linkSpeed+" Megabits per second\n");
//
//        }
//
//        // Location
////        loc2 = (TextView) findViewById(R.id.loc2);
////        googleApiClient = new GoogleApiClient.Builder(this)
////                .addApi(LocationServices.API)
////                .addConnectionCallbacks(this)
////                .addOnConnectionFailedListener(this).build();
////
////        locationRequest = new LocationRequest();
////        locationRequest.setInterval(10 * 1000); // save battery by checking every 10 seconds
////        locationRequest.setFastestInterval(15 * 1000);
////        locationRequest.setPriority(LocationRequest.PRIORITY_BALANCED_POWER_ACCURACY);
//    }
//
//    // Method to get account name
//    public static Account getAccount(AccountManager accountManager) {
//        Account[] accounts = accountManager.getAccountsByType("com.google");
//        Account account;
//        if (accounts.length > 0) {
//            account = accounts[0];
//        } else {
//            account = null;
//        }
//        return account;
//    }
//
//    public static void getInternet() {
//        StrictMode.ThreadPolicy policy = new StrictMode.ThreadPolicy.Builder().permitAll().build();
//        StrictMode.setThreadPolicy(policy);
//    }
//
//    public static String readKernelVersion() {
//        try {
//            Process p = Runtime.getRuntime().exec("uname -a");
//            InputStream is = null;
//            if (p.waitFor() == 0) {
//                is = p.getInputStream();
//            } else {
//                is = p.getErrorStream();
//            }
//            BufferedReader br = new BufferedReader(new InputStreamReader(is), 1024);
//            String line = br.readLine();
//            br.close();
//            return line;
//        } catch (Exception ex) {
//            return "ERROR: " + ex.getMessage();
//        }
//    }
//
//
//    public static String getDeviceModelNumber() {
//        String manufacturer = Build.VERSION.CODENAME;
//        String model = Build.MODEL;
//        if (model.startsWith(manufacturer)) {
//            return capitalize(model);
//        } else {
//            return capitalize(manufacturer) + " " + model;
//        }
//    }
//
//    private static String capitalize(String s) {
//        if (s == null || s.length() == 0) {
//            return "";
//        }
//        char first = s.charAt(0);
//        if (Character.isUpperCase(first)) {
//            return s;
//        } else {
//            return Character.toUpperCase(first) + s.substring(1);
//        }
//    }
//
//    // -------------------------------------------------------------------------------------
//    // HTTP POST DATA
//
//
//    public void receive(String info_text) {
//
//        DroneTest req = new DroneTest();
//        Toast.makeText(getApplicationContext(), info_text, Toast.LENGTH_SHORT).show();
//        req.execute(info_text);
//    }
//
//    @Override
//    public void onConnected(@Nullable Bundle bundle) {
//        requestLocationUpdates();
//    }
//
//    private void requestLocationUpdates() {
//        if (ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_FINE_LOCATION) != PackageManager.PERMISSION_GRANTED && ActivityCompat.checkSelfPermission(this, android.Manifest.permission.ACCESS_COARSE_LOCATION) != PackageManager.PERMISSION_GRANTED) {
//            // TODO: Consider calling
//            //    ActivityCompat#requestPermissions
//            // here to request the missing permissions, and then overriding
//            //   public void onRequestPermissionsResult(int requestCode, String[] permissions,
//            //                                          int[] grantResults)
//            // to handle the case where the user grants the permission. See the documentation
//            // for ActivityCompat#requestPermissions for more details.
//            return;
//        }
//        LocationServices.FusedLocationApi.requestLocationUpdates(googleApiClient, locationRequest, this);
//    }
//
//    @Override
//    public void onConnectionSuspended(int i) {
//
//    }
//
//    @Override
//    public void onConnectionFailed(@NonNull ConnectionResult connectionResult) {
//
//    }
//
//    @Override
//    public void onLocationChanged(Location location) {
//        Double myLatitude = location.getLatitude();
//        Double myLongitude = location.getLongitude();
//        loc2.setText("Latitude : " + String.valueOf(myLatitude)+"\nLongitude : " + String.valueOf(myLongitude));
//    }
//
//    @Override
//    protected void onStart() {
//        super.onStart();
//        googleApiClient.connect();
//    }
//
//    @Override
//    protected void onResume() {
//        super.onResume();
//        if (googleApiClient.isConnected()) {
//            requestLocationUpdates();
//        }
//    }
//
//    @Override
//    protected void onPause() {
//        super.onPause();
//        LocationServices.FusedLocationApi.removeLocationUpdates(googleApiClient, this);
//    }
//
//    @Override
//    protected void onStop() {
//        super.onStop();
//        googleApiClient.disconnect();
//    }
//
//
//    public class DroneTest extends AsyncTask<String, Integer, String> {
//        @Override
//        protected void onPreExecute() {
//
//        }
//
//        @Override
//        protected String doInBackground(String... params) {
//            // TODO Auto-generated method stub
//            // Call your web service here
//            String android_id =Settings.Secure.getString(getContentResolver(),Settings.Secure.ANDROID_ID);
//            String ip_ = "192.168.1.106";
//            String port_ = ":8080";
//            String targetURL = "http://"+ ip_ + port_ +"/" ;
//            String urlParameters = android_id ;
//
//            // Getting data
//            String OSNAME = System.getProperty("os.name");
//
//            HttpURLConnection connection = null;
//
//            try {
//                //Create connection
//
//                URL url = new URL(targetURL);
//                connection = (HttpURLConnection) url.openConnection();
//                connection.setRequestMethod("POST");
//                connection.setRequestProperty("Content-Type",
//                        "application/x-www-form-urlencoded");
//
//                connection.setRequestProperty("Content-Length",
//                        Integer.toString(urlParameters.getBytes().length));
//                connection.setRequestProperty("Content-Language", "en-US");
//
//                connection.setUseCaches(false);
//                connection.setDoOutput(true);
//
//                //Send request
//                DataOutputStream wr = new DataOutputStream (
//                        connection.getOutputStream());
//                wr.writeBytes(urlParameters);
//                //wr.writeBytes(OSNAME);
//                wr.close();
//
//                //Get Response
//                InputStream is = connection.getInputStream();
//                BufferedReader rd = new BufferedReader(new InputStreamReader(is));
//                StringBuilder response = new StringBuilder(); // or StringBuffer if Java version 5+
//                String line;
//                while ((line = rd.readLine()) != null) {
//                    response.append(line);
//                    response.append('\r');
//                }
//                rd.close();
//                Toast.makeText(getApplicationContext(),"Connection success!",Toast.LENGTH_LONG).show();
//
//                return response.toString();
//            } catch (Exception e) {
//                e.printStackTrace();
//                return null;
//            } finally {
//                if (connection != null) {
//                    connection.disconnect();
//                }
//            }
//        }
//
//        @Override
//        protected void onPostExecute(String result) {
//            // TODO Auto-generated method stub
//            // Update your UI here
//            //Toast.makeText(getApplicationContext(),"Howdy!",Toast.LENGTH_SHORT).show();
//            return;
//        }
//    }
//
//    // -------------------------------------------------------------------------------------
//
//
//}
