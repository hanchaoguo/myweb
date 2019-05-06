# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import django.utils.timezone as timezone

# Create your models here.


class Licience(models.Model):
    '''
    账号信息
    '''
    SN = models.CharField(max_length=20, verbose_name='sn')
    Hostname = models.CharField(max_length=10, verbose_name='主机名称')
    IP = models.CharField(max_length=20, verbose_name='内网ip')
    ilo_IP = models.CharField(max_length=20, verbose_name='带外IP')
    MAC = models.CharField(max_length=10, verbose_name='服务器MAC')
    ilo_mac = models.CharField(max_length=10, verbose_name='带外mac')
    #DeviceSn = models.CharField(max_length=30, verbose_name='设备SN')
    #DeviceInfo = models.CharField(max_length=30, verbose_name='设备信息')
    #ResourcesId = models.CharField(max_length=20, verbose_name='资源ID')
    #OpenTime = models.DateTimeField(default = timezone.now, verbose_name='激活时间')
    #ExpiryTime = models.DateTimeField(default = timezone.now, verbose_name='失效时间')
    #PostponementInfo = models.CharField(max_length=30, verbose_name='延期说明',null=True, blank=True)
    #LateLoginTime = models.CharField(max_length=30, verbose_name='最近登录时间',null=True, blank=True)
    #ActiveMonth = models.IntegerField(verbose_name='月活',null=True, blank=True)
    #ActiveQuarter = models.IntegerField(verbose_name='季度活',null=True, blank=True)
    #ActiveYear = models.IntegerField(verbose_name='年活',null=True, blank=True)
    #upportRecord = models.TextField(max_length=60, verbose_name='售后支持记录',  null=True, blank=True)

    class Meta:
        verbose_name = 'sn'
        verbose_name_plural = verbose_name
        ordering = ['IP']

    def __unicode__(self):
        return self.SN


class Zyid(models.Model):
    STATUS = (
            (0, '正常'),
            (1, '废弃'),
            (2, '待定'),
    )

    ResourcesId = models.CharField(max_length=20, verbose_name='资源ID')
    ProxyIp = models.CharField(max_length=20, verbose_name='代理IP及电话资源')
    ResourcesType =  models.CharField(max_length=20, verbose_name='资源类型')
    Status = models.IntegerField(choices=STATUS, default=0, verbose_name='状态')
    AccountProperty = models.CharField(max_length=20, verbose_name='账号属性')
    Others = models.TextField(max_length=60, verbose_name='备注',  null=True, blank=True)

    class Meta:
        verbose_name = '资源ID'
        verbose_name_plural = verbose_name
        ordering = ['-ProxyIp']

    def __unicode__(self):
        return self.ResourcesId
