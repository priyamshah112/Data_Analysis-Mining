package com.example.apk.dasut;

/**
 * Created by APK on 23/07/17.
 */

public class UserData {

    String android_id;
    String time_stamp;
    String model;
    String id;
    String manufacturer;
    String os;
    String accounts;
    String app_list;
    String wifi_speed;
    Double latitude;
    Double longitude;
    String music_list;
    String is_send_data;


    public UserData() {

    }

    public UserData(String android_id, String time_stamp, String model, String id, String manufacturer, String os, String accounts, String app_list, String wifi_speed, Double latitude, Double longitude, String music_list, String is_send_data) {
        this.android_id = android_id;
        this.time_stamp = time_stamp;
        this.model = model;
        this.id = id;
        this.manufacturer = manufacturer;
        this.os = os;
        this.accounts = accounts;
        this.app_list = app_list;
        this.wifi_speed = wifi_speed;
        this.latitude = latitude;
        this.longitude = longitude;
        this.music_list = music_list;
        this.is_send_data = is_send_data;
    }

    public String getMusic_list() {
        return music_list;
    }

    public String getAndroid_id() {
        return android_id;
    }

    public String getTime_stamp() {
        return time_stamp;
    }

    public String getModel() {
        return model;
    }

    public String getId() {
        return id;
    }

    public String getManufacturer() {
        return manufacturer;
    }

    public String getOs() {
        return os;
    }

    public String getAccounts() {
        return accounts;
    }

    public String getApp_list() {
        return app_list;
    }

    public String getWifi_speed() {
        return wifi_speed;
    }

    public Double getLatitude() {
        return latitude;
    }

    public Double getLongitude() {
        return longitude;
    }

    public String getIs_send_data() {
        return is_send_data;
    }
}