package com.example.blinknotificationlistener;

import android.content.Intent;
import android.os.IBinder;

import androidx.annotation.Nullable;

public class NotificationListener extends android.app.Service {

    @Nullable
    @Override
    public IBinder onBind(Intent intent) {
        return null;
    }
}
