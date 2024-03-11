# -*- coding: utf8 -*-
# Copyright (c) 2017-2021 THL A29 Limited, a Tencent company. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import warnings

from tencentcloud.common.abstract_model import AbstractModel


class Condition(AbstractModel):
    """- [ ] 过滤条件<br>

    <li>Name - String - 是否必填：否 - 操作符: ilike  - 排序支持：否- 根据分组名称进行查询。</li>
    分页参数<br>
    <li>PageNum 从1开始，小于等于0时使用默认参数。</li>
    <li>PageSize 最大值5000，最好不超过100。</li>

    """

    def __init__(self):
        r"""
        :param _Filters: Filters 条件过滤
注意：此字段可能返回 null，表示取不到有效值。
        :type Filters: list of Filter
        :param _FilterGroups: FilterGroups 条件过滤组
注意：此字段可能返回 null，表示取不到有效值。
        :type FilterGroups: list of FilterGroup
        :param _Sort: Sort 排序字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Sort: :class:`tencentcloud.ioa.v20220601.models.Sort`
        :param _PageSize: PageSize 每页获取数(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _PageNum: PageNum 获取第几页(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNum: int
        """
        self._Filters = None
        self._FilterGroups = None
        self._Sort = None
        self._PageSize = None
        self._PageNum = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def FilterGroups(self):
        return self._FilterGroups

    @FilterGroups.setter
    def FilterGroups(self, FilterGroups):
        self._FilterGroups = FilterGroups

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("FilterGroups") is not None:
            self._FilterGroups = []
            for item in params.get("FilterGroups"):
                obj = FilterGroup()
                obj._deserialize(item)
                self._FilterGroups.append(obj)
        if params.get("Sort") is not None:
            self._Sort = Sort()
            self._Sort._deserialize(params.get("Sort"))
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesPageRsp(AbstractModel):
    """分页的data数据

    """

    def __init__(self):
        r"""
        :param _Paging: 数据分页信息
注意：此字段可能返回 null，表示取不到有效值。
        :type Paging: :class:`tencentcloud.ioa.v20220601.models.Paging`
        :param _Items: 业务响应数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Items: list of DeviceDetail
        """
        self._Paging = None
        self._Items = None

    @property
    def Paging(self):
        return self._Paging

    @Paging.setter
    def Paging(self, Paging):
        self._Paging = Paging

    @property
    def Items(self):
        return self._Items

    @Items.setter
    def Items(self, Items):
        self._Items = Items


    def _deserialize(self, params):
        if params.get("Paging") is not None:
            self._Paging = Paging()
            self._Paging._deserialize(params.get("Paging"))
        if params.get("Items") is not None:
            self._Items = []
            for item in params.get("Items"):
                obj = DeviceDetail()
                obj._deserialize(item)
                self._Items.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesRequest(AbstractModel):
    """DescribeDevices请求参数结构体

    """

    def __init__(self):
        r"""
        :param _Condition: 过滤条件<br>
<li>Ip - String - 是否必填：否 - 操作符: eq  - 排序支持：否- 按照Ip进行过滤。</li>
<li>MacAddr - String - 是否必填：否 - 操作符: eq  - 排序支持：否- 按照mac地址进行过滤。</li>
<li>IoaUserName - String - 是否必填：否 - 操作符: eq  - 排序支持：否- 按照ioa用户名进行过滤。</li>
分页参数<br>
<li>PageNum 从1开始，小于等于0时使用默认参数。</li>
<li>PageSize 最大值5000，最好不超过100。</li>
        :type Condition: :class:`tencentcloud.ioa.v20220601.models.Condition`
        :param _GroupId: 私有化默认分组id-名称-操作系统
1	全网终端	Win
2	未分组终端	Win
30000000	服务器	Win
40000101	全网终端	Linux
40000102	未分组终端	Linux
40000103	服务器	Linux
40000201	全网终端	macOS
40000202	未分组终端	macOS
40000203	服务器	macOS
40000401	全网终端	Android
40000402	未分组终端	Android
40000501	全网终端	iOS
40000502	未分组终端	iOS
        :type GroupId: int
        :param _OsType: 系统类型（0: win，1：linux，2: mac，3: win_srv，4：android，5：ios   默认值0）
        :type OsType: int
        :param _OnlineStatus: 在线状态 2 在线 0，1 离线
        :type OnlineStatus: int
        :param _Filters: 过滤条件--兼容旧接口,参数同Condition
        :type Filters: list of Filter
        :param _Sort: 排序字段--兼容旧接口,参数同Condition
        :type Sort: :class:`tencentcloud.ioa.v20220601.models.Sort`
        :param _PageNum: 获取第几页--兼容旧接口,参数同Condition(只支持32位)
        :type PageNum: int
        :param _PageSize: 每页获取数--兼容旧接口,参数同Condition(只支持32位)
        :type PageSize: int
        :param _Status: 授权状态 4未授权 5已授权
        :type Status: int
        """
        self._Condition = None
        self._GroupId = None
        self._OsType = None
        self._OnlineStatus = None
        self._Filters = None
        self._Sort = None
        self._PageNum = None
        self._PageSize = None
        self._Status = None

    @property
    def Condition(self):
        return self._Condition

    @Condition.setter
    def Condition(self, Condition):
        self._Condition = Condition

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def OsType(self):
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def OnlineStatus(self):
        return self._OnlineStatus

    @OnlineStatus.setter
    def OnlineStatus(self, OnlineStatus):
        self._OnlineStatus = OnlineStatus

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters

    @property
    def Sort(self):
        return self._Sort

    @Sort.setter
    def Sort(self, Sort):
        self._Sort = Sort

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def Status(self):
        return self._Status

    @Status.setter
    def Status(self, Status):
        self._Status = Status


    def _deserialize(self, params):
        if params.get("Condition") is not None:
            self._Condition = Condition()
            self._Condition._deserialize(params.get("Condition"))
        self._GroupId = params.get("GroupId")
        self._OsType = params.get("OsType")
        self._OnlineStatus = params.get("OnlineStatus")
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        if params.get("Sort") is not None:
            self._Sort = Sort()
            self._Sort._deserialize(params.get("Sort"))
        self._PageNum = params.get("PageNum")
        self._PageSize = params.get("PageSize")
        self._Status = params.get("Status")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class DescribeDevicesResponse(AbstractModel):
    """DescribeDevices返回参数结构体

    """

    def __init__(self):
        r"""
        :param _Data: 分页的data数据
注意：此字段可能返回 null，表示取不到有效值。
        :type Data: :class:`tencentcloud.ioa.v20220601.models.DescribeDevicesPageRsp`
        :param _RequestId: 唯一请求 ID，由服务端生成，每次请求都会返回（若请求因其他原因未能抵达服务端，则该次请求不会获得 RequestId）。定位问题时需要提供该次请求的 RequestId。
        :type RequestId: str
        """
        self._Data = None
        self._RequestId = None

    @property
    def Data(self):
        return self._Data

    @Data.setter
    def Data(self, Data):
        self._Data = Data

    @property
    def RequestId(self):
        return self._RequestId

    @RequestId.setter
    def RequestId(self, RequestId):
        self._RequestId = RequestId


    def _deserialize(self, params):
        if params.get("Data") is not None:
            self._Data = DescribeDevicesPageRsp()
            self._Data._deserialize(params.get("Data"))
        self._RequestId = params.get("RequestId")


class DeviceDetail(AbstractModel):
    """业务响应数据

    """

    def __init__(self):
        r"""
        :param _Id: 设备ID(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type Id: int
        :param _Mid: 设备唯一标识符
注意：此字段可能返回 null，表示取不到有效值。
        :type Mid: str
        :param _Name: 终端名（设备名）
注意：此字段可能返回 null，表示取不到有效值。
        :type Name: str
        :param _GroupId: 设备所在分组ID(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupId: int
        :param _OsType: OS平台(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type OsType: int
        :param _Ip: 设备IP地址（出口IP）
注意：此字段可能返回 null，表示取不到有效值。
        :type Ip: str
        :param _OnlineStatus: 在线状态 2 在线 0，1 离线(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type OnlineStatus: int
        :param _Version: 客户端版本号-大整数
注意：此字段可能返回 null，表示取不到有效值。
        :type Version: str
        :param _StrVersion: 客户端版本号-点分字符串
注意：此字段可能返回 null，表示取不到有效值。
        :type StrVersion: str
        :param _Itime: 首次在线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type Itime: str
        :param _ConnActiveTime: 最后一次在线时间
注意：此字段可能返回 null，表示取不到有效值。
        :type ConnActiveTime: str
        :param _Locked: 设备是否加锁 1 锁定 0 2 非锁定(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type Locked: int
        :param _LocalIpList: 设备本地IP列表, 包括IP
注意：此字段可能返回 null，表示取不到有效值。
        :type LocalIpList: str
        :param _HostId: 主机ID(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type HostId: int
        :param _GroupName: 设备所属分组名
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupName: str
        :param _GroupNamePath: 设备所属分组路径
注意：此字段可能返回 null，表示取不到有效值。
        :type GroupNamePath: str
        :param _CriticalVulListCount: 未修复高危漏洞数(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type CriticalVulListCount: int
        :param _ComputerName: 设备名 和Name相同，保留参数
注意：此字段可能返回 null，表示取不到有效值。
        :type ComputerName: str
        :param _DomainName: 登录域名
注意：此字段可能返回 null，表示取不到有效值。
        :type DomainName: str
        :param _MacAddr: MAC地址
注意：此字段可能返回 null，表示取不到有效值。
        :type MacAddr: str
        :param _VulCount: 漏洞数(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type VulCount: int
        :param _RiskCount: 病毒风险数(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type RiskCount: int
        :param _VirusVer: 病毒库版本
注意：此字段可能返回 null，表示取不到有效值。
        :type VirusVer: str
        :param _VulVersion: 漏洞库版本
注意：此字段可能返回 null，表示取不到有效值。
        :type VulVersion: str
        :param _SysRepVersion: 系统修复引擎版本
注意：此字段可能返回 null，表示取不到有效值。
        :type SysRepVersion: str
        :param _VulCriticalList: 高危补丁列表
注意：此字段可能返回 null，表示取不到有效值。
        :type VulCriticalList: list of str
        :param _Tags: 标签
注意：此字段可能返回 null，表示取不到有效值。
        :type Tags: str
        :param _UserName: 终端用户名
注意：此字段可能返回 null，表示取不到有效值。
        :type UserName: str
        :param _FirewallStatus: 防火墙状态(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type FirewallStatus: int
        :param _SerialNum: SN序列号
注意：此字段可能返回 null，表示取不到有效值。
        :type SerialNum: str
        :param _DeviceStrategyVer: 设备管控策略版本
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceStrategyVer: str
        :param _NGNStrategyVer: NGN策略版本
注意：此字段可能返回 null，表示取不到有效值。
        :type NGNStrategyVer: str
        :param _IOAUserName: 最近登录账号
注意：此字段可能返回 null，表示取不到有效值。
        :type IOAUserName: str
        :param _DeviceNewStrategyVer: 设备管控新策略
注意：此字段可能返回 null，表示取不到有效值。
        :type DeviceNewStrategyVer: str
        :param _NGNNewStrategyVer: NGN策略新版本
注意：此字段可能返回 null，表示取不到有效值。
        :type NGNNewStrategyVer: str
        :param _HostName: 主机名称
注意：此字段可能返回 null，表示取不到有效值。
        :type HostName: str
        :param _BaseBoardSn: 主板序列号
注意：此字段可能返回 null，表示取不到有效值。
        :type BaseBoardSn: str
        :param _AccountUsers: 绑定账户只有名字
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountUsers: str
        :param _IdentityStrategyVer: 身份策略版本
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityStrategyVer: str
        :param _IdentityNewStrategyVer: 身份策略新版本
注意：此字段可能返回 null，表示取不到有效值。
        :type IdentityNewStrategyVer: str
        :param _AccountGroupName: 最近登录账号部门
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountGroupName: str
        :param _AccountName: 登录账号姓名
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountName: str
        :param _AccountGroupId: 账号组id
注意：此字段可能返回 null，表示取不到有效值。
        :type AccountGroupId: int
        """
        self._Id = None
        self._Mid = None
        self._Name = None
        self._GroupId = None
        self._OsType = None
        self._Ip = None
        self._OnlineStatus = None
        self._Version = None
        self._StrVersion = None
        self._Itime = None
        self._ConnActiveTime = None
        self._Locked = None
        self._LocalIpList = None
        self._HostId = None
        self._GroupName = None
        self._GroupNamePath = None
        self._CriticalVulListCount = None
        self._ComputerName = None
        self._DomainName = None
        self._MacAddr = None
        self._VulCount = None
        self._RiskCount = None
        self._VirusVer = None
        self._VulVersion = None
        self._SysRepVersion = None
        self._VulCriticalList = None
        self._Tags = None
        self._UserName = None
        self._FirewallStatus = None
        self._SerialNum = None
        self._DeviceStrategyVer = None
        self._NGNStrategyVer = None
        self._IOAUserName = None
        self._DeviceNewStrategyVer = None
        self._NGNNewStrategyVer = None
        self._HostName = None
        self._BaseBoardSn = None
        self._AccountUsers = None
        self._IdentityStrategyVer = None
        self._IdentityNewStrategyVer = None
        self._AccountGroupName = None
        self._AccountName = None
        self._AccountGroupId = None

    @property
    def Id(self):
        return self._Id

    @Id.setter
    def Id(self, Id):
        self._Id = Id

    @property
    def Mid(self):
        return self._Mid

    @Mid.setter
    def Mid(self, Mid):
        self._Mid = Mid

    @property
    def Name(self):
        return self._Name

    @Name.setter
    def Name(self, Name):
        self._Name = Name

    @property
    def GroupId(self):
        return self._GroupId

    @GroupId.setter
    def GroupId(self, GroupId):
        self._GroupId = GroupId

    @property
    def OsType(self):
        return self._OsType

    @OsType.setter
    def OsType(self, OsType):
        self._OsType = OsType

    @property
    def Ip(self):
        return self._Ip

    @Ip.setter
    def Ip(self, Ip):
        self._Ip = Ip

    @property
    def OnlineStatus(self):
        return self._OnlineStatus

    @OnlineStatus.setter
    def OnlineStatus(self, OnlineStatus):
        self._OnlineStatus = OnlineStatus

    @property
    def Version(self):
        return self._Version

    @Version.setter
    def Version(self, Version):
        self._Version = Version

    @property
    def StrVersion(self):
        return self._StrVersion

    @StrVersion.setter
    def StrVersion(self, StrVersion):
        self._StrVersion = StrVersion

    @property
    def Itime(self):
        return self._Itime

    @Itime.setter
    def Itime(self, Itime):
        self._Itime = Itime

    @property
    def ConnActiveTime(self):
        return self._ConnActiveTime

    @ConnActiveTime.setter
    def ConnActiveTime(self, ConnActiveTime):
        self._ConnActiveTime = ConnActiveTime

    @property
    def Locked(self):
        return self._Locked

    @Locked.setter
    def Locked(self, Locked):
        self._Locked = Locked

    @property
    def LocalIpList(self):
        return self._LocalIpList

    @LocalIpList.setter
    def LocalIpList(self, LocalIpList):
        self._LocalIpList = LocalIpList

    @property
    def HostId(self):
        return self._HostId

    @HostId.setter
    def HostId(self, HostId):
        self._HostId = HostId

    @property
    def GroupName(self):
        return self._GroupName

    @GroupName.setter
    def GroupName(self, GroupName):
        self._GroupName = GroupName

    @property
    def GroupNamePath(self):
        return self._GroupNamePath

    @GroupNamePath.setter
    def GroupNamePath(self, GroupNamePath):
        self._GroupNamePath = GroupNamePath

    @property
    def CriticalVulListCount(self):
        return self._CriticalVulListCount

    @CriticalVulListCount.setter
    def CriticalVulListCount(self, CriticalVulListCount):
        self._CriticalVulListCount = CriticalVulListCount

    @property
    def ComputerName(self):
        return self._ComputerName

    @ComputerName.setter
    def ComputerName(self, ComputerName):
        self._ComputerName = ComputerName

    @property
    def DomainName(self):
        return self._DomainName

    @DomainName.setter
    def DomainName(self, DomainName):
        self._DomainName = DomainName

    @property
    def MacAddr(self):
        return self._MacAddr

    @MacAddr.setter
    def MacAddr(self, MacAddr):
        self._MacAddr = MacAddr

    @property
    def VulCount(self):
        return self._VulCount

    @VulCount.setter
    def VulCount(self, VulCount):
        self._VulCount = VulCount

    @property
    def RiskCount(self):
        return self._RiskCount

    @RiskCount.setter
    def RiskCount(self, RiskCount):
        self._RiskCount = RiskCount

    @property
    def VirusVer(self):
        return self._VirusVer

    @VirusVer.setter
    def VirusVer(self, VirusVer):
        self._VirusVer = VirusVer

    @property
    def VulVersion(self):
        return self._VulVersion

    @VulVersion.setter
    def VulVersion(self, VulVersion):
        self._VulVersion = VulVersion

    @property
    def SysRepVersion(self):
        return self._SysRepVersion

    @SysRepVersion.setter
    def SysRepVersion(self, SysRepVersion):
        self._SysRepVersion = SysRepVersion

    @property
    def VulCriticalList(self):
        return self._VulCriticalList

    @VulCriticalList.setter
    def VulCriticalList(self, VulCriticalList):
        self._VulCriticalList = VulCriticalList

    @property
    def Tags(self):
        return self._Tags

    @Tags.setter
    def Tags(self, Tags):
        self._Tags = Tags

    @property
    def UserName(self):
        return self._UserName

    @UserName.setter
    def UserName(self, UserName):
        self._UserName = UserName

    @property
    def FirewallStatus(self):
        return self._FirewallStatus

    @FirewallStatus.setter
    def FirewallStatus(self, FirewallStatus):
        self._FirewallStatus = FirewallStatus

    @property
    def SerialNum(self):
        return self._SerialNum

    @SerialNum.setter
    def SerialNum(self, SerialNum):
        self._SerialNum = SerialNum

    @property
    def DeviceStrategyVer(self):
        return self._DeviceStrategyVer

    @DeviceStrategyVer.setter
    def DeviceStrategyVer(self, DeviceStrategyVer):
        self._DeviceStrategyVer = DeviceStrategyVer

    @property
    def NGNStrategyVer(self):
        return self._NGNStrategyVer

    @NGNStrategyVer.setter
    def NGNStrategyVer(self, NGNStrategyVer):
        self._NGNStrategyVer = NGNStrategyVer

    @property
    def IOAUserName(self):
        return self._IOAUserName

    @IOAUserName.setter
    def IOAUserName(self, IOAUserName):
        self._IOAUserName = IOAUserName

    @property
    def DeviceNewStrategyVer(self):
        return self._DeviceNewStrategyVer

    @DeviceNewStrategyVer.setter
    def DeviceNewStrategyVer(self, DeviceNewStrategyVer):
        self._DeviceNewStrategyVer = DeviceNewStrategyVer

    @property
    def NGNNewStrategyVer(self):
        return self._NGNNewStrategyVer

    @NGNNewStrategyVer.setter
    def NGNNewStrategyVer(self, NGNNewStrategyVer):
        self._NGNNewStrategyVer = NGNNewStrategyVer

    @property
    def HostName(self):
        return self._HostName

    @HostName.setter
    def HostName(self, HostName):
        self._HostName = HostName

    @property
    def BaseBoardSn(self):
        return self._BaseBoardSn

    @BaseBoardSn.setter
    def BaseBoardSn(self, BaseBoardSn):
        self._BaseBoardSn = BaseBoardSn

    @property
    def AccountUsers(self):
        return self._AccountUsers

    @AccountUsers.setter
    def AccountUsers(self, AccountUsers):
        self._AccountUsers = AccountUsers

    @property
    def IdentityStrategyVer(self):
        return self._IdentityStrategyVer

    @IdentityStrategyVer.setter
    def IdentityStrategyVer(self, IdentityStrategyVer):
        self._IdentityStrategyVer = IdentityStrategyVer

    @property
    def IdentityNewStrategyVer(self):
        return self._IdentityNewStrategyVer

    @IdentityNewStrategyVer.setter
    def IdentityNewStrategyVer(self, IdentityNewStrategyVer):
        self._IdentityNewStrategyVer = IdentityNewStrategyVer

    @property
    def AccountGroupName(self):
        return self._AccountGroupName

    @AccountGroupName.setter
    def AccountGroupName(self, AccountGroupName):
        self._AccountGroupName = AccountGroupName

    @property
    def AccountName(self):
        return self._AccountName

    @AccountName.setter
    def AccountName(self, AccountName):
        self._AccountName = AccountName

    @property
    def AccountGroupId(self):
        return self._AccountGroupId

    @AccountGroupId.setter
    def AccountGroupId(self, AccountGroupId):
        self._AccountGroupId = AccountGroupId


    def _deserialize(self, params):
        self._Id = params.get("Id")
        self._Mid = params.get("Mid")
        self._Name = params.get("Name")
        self._GroupId = params.get("GroupId")
        self._OsType = params.get("OsType")
        self._Ip = params.get("Ip")
        self._OnlineStatus = params.get("OnlineStatus")
        self._Version = params.get("Version")
        self._StrVersion = params.get("StrVersion")
        self._Itime = params.get("Itime")
        self._ConnActiveTime = params.get("ConnActiveTime")
        self._Locked = params.get("Locked")
        self._LocalIpList = params.get("LocalIpList")
        self._HostId = params.get("HostId")
        self._GroupName = params.get("GroupName")
        self._GroupNamePath = params.get("GroupNamePath")
        self._CriticalVulListCount = params.get("CriticalVulListCount")
        self._ComputerName = params.get("ComputerName")
        self._DomainName = params.get("DomainName")
        self._MacAddr = params.get("MacAddr")
        self._VulCount = params.get("VulCount")
        self._RiskCount = params.get("RiskCount")
        self._VirusVer = params.get("VirusVer")
        self._VulVersion = params.get("VulVersion")
        self._SysRepVersion = params.get("SysRepVersion")
        self._VulCriticalList = params.get("VulCriticalList")
        self._Tags = params.get("Tags")
        self._UserName = params.get("UserName")
        self._FirewallStatus = params.get("FirewallStatus")
        self._SerialNum = params.get("SerialNum")
        self._DeviceStrategyVer = params.get("DeviceStrategyVer")
        self._NGNStrategyVer = params.get("NGNStrategyVer")
        self._IOAUserName = params.get("IOAUserName")
        self._DeviceNewStrategyVer = params.get("DeviceNewStrategyVer")
        self._NGNNewStrategyVer = params.get("NGNNewStrategyVer")
        self._HostName = params.get("HostName")
        self._BaseBoardSn = params.get("BaseBoardSn")
        self._AccountUsers = params.get("AccountUsers")
        self._IdentityStrategyVer = params.get("IdentityStrategyVer")
        self._IdentityNewStrategyVer = params.get("IdentityNewStrategyVer")
        self._AccountGroupName = params.get("AccountGroupName")
        self._AccountName = params.get("AccountName")
        self._AccountGroupId = params.get("AccountGroupId")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Filter(AbstractModel):
    """Filters 条件过滤

    """

    def __init__(self):
        r"""
        :param _Field: 过滤字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Field: str
        :param _Operator: 过滤方式 eq:等于,net:不等于,like,nlike,gt:大于,lt:小于,egt:大于等于,elt:小于等于
注意：此字段可能返回 null，表示取不到有效值。
        :type Operator: str
        :param _Values: 过滤条件
注意：此字段可能返回 null，表示取不到有效值。
        :type Values: list of str
        """
        self._Field = None
        self._Operator = None
        self._Values = None

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Operator(self):
        return self._Operator

    @Operator.setter
    def Operator(self, Operator):
        self._Operator = Operator

    @property
    def Values(self):
        return self._Values

    @Values.setter
    def Values(self, Values):
        self._Values = Values


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Operator = params.get("Operator")
        self._Values = params.get("Values")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class FilterGroup(AbstractModel):
    """FilterGroups 条件过滤组

    """

    def __init__(self):
        r"""
        :param _Filters: Filters 条件过滤
注意：此字段可能返回 null，表示取不到有效值。
        :type Filters: list of Filter
        """
        self._Filters = None

    @property
    def Filters(self):
        return self._Filters

    @Filters.setter
    def Filters(self, Filters):
        self._Filters = Filters


    def _deserialize(self, params):
        if params.get("Filters") is not None:
            self._Filters = []
            for item in params.get("Filters"):
                obj = Filter()
                obj._deserialize(item)
                self._Filters.append(obj)
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Paging(AbstractModel):
    """数据分页信息

    """

    def __init__(self):
        r"""
        :param _PageSize: 每页条数(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type PageSize: int
        :param _PageNum: 页码(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type PageNum: int
        :param _PageCount: 总页数(只支持32位)
注意：此字段可能返回 null，表示取不到有效值。
        :type PageCount: int
        :param _Total: 记录总数
注意：此字段可能返回 null，表示取不到有效值。
        :type Total: int
        """
        self._PageSize = None
        self._PageNum = None
        self._PageCount = None
        self._Total = None

    @property
    def PageSize(self):
        return self._PageSize

    @PageSize.setter
    def PageSize(self, PageSize):
        self._PageSize = PageSize

    @property
    def PageNum(self):
        return self._PageNum

    @PageNum.setter
    def PageNum(self, PageNum):
        self._PageNum = PageNum

    @property
    def PageCount(self):
        return self._PageCount

    @PageCount.setter
    def PageCount(self, PageCount):
        self._PageCount = PageCount

    @property
    def Total(self):
        return self._Total

    @Total.setter
    def Total(self, Total):
        self._Total = Total


    def _deserialize(self, params):
        self._PageSize = params.get("PageSize")
        self._PageNum = params.get("PageNum")
        self._PageCount = params.get("PageCount")
        self._Total = params.get("Total")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        


class Sort(AbstractModel):
    """Sort 排序字段

    """

    def __init__(self):
        r"""
        :param _Field: 排序字段
注意：此字段可能返回 null，表示取不到有效值。
        :type Field: str
        :param _Order: 排序方式
注意：此字段可能返回 null，表示取不到有效值。
        :type Order: str
        """
        self._Field = None
        self._Order = None

    @property
    def Field(self):
        return self._Field

    @Field.setter
    def Field(self, Field):
        self._Field = Field

    @property
    def Order(self):
        return self._Order

    @Order.setter
    def Order(self, Order):
        self._Order = Order


    def _deserialize(self, params):
        self._Field = params.get("Field")
        self._Order = params.get("Order")
        memeber_set = set(params.keys())
        for name, value in vars(self).items():
            property_name = name[1:]
            if property_name in memeber_set:
                memeber_set.remove(property_name)
        if len(memeber_set) > 0:
            warnings.warn("%s fileds are useless." % ",".join(memeber_set))
        