# coding=utf-8
# *** WARNING: this file was generated by pulumi-language-python. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import copy
import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from .. import _utilities

__all__ = [
    'ValidatorFlagsArgs',
    'ValidatorKeyPairsArgs',
    'ValidatorPathsArgs',
]

@pulumi.input_type
class ValidatorFlagsArgs:
    def __init__(__self__, *,
                 block_production_method: pulumi.Input[str],
                 dynamic_port_range: pulumi.Input[str],
                 full_snapshot_interval_slots: pulumi.Input[int],
                 gossip_port: pulumi.Input[int],
                 limit_ledger_size: pulumi.Input[int],
                 no_wait_for_vote_to_start_leader: pulumi.Input[bool],
                 only_known_rpc: pulumi.Input[bool],
                 paths: pulumi.Input['ValidatorPathsArgs'],
                 private_rpc: pulumi.Input[bool],
                 rpc_bind_address: pulumi.Input[str],
                 rpc_port: pulumi.Input[int],
                 use_snapshot_archives_at_startup: pulumi.Input[str],
                 wal_recovery_mode: pulumi.Input[str],
                 entry_point: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 expected_genesis_hash: Optional[pulumi.Input[str]] = None,
                 full_rpc_api: Optional[pulumi.Input[bool]] = None,
                 known_validator: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]] = None,
                 no_voting: Optional[pulumi.Input[bool]] = None,
                 tvu_receive_threads: Optional[pulumi.Input[int]] = None):
        pulumi.set(__self__, "block_production_method", block_production_method)
        pulumi.set(__self__, "dynamic_port_range", dynamic_port_range)
        pulumi.set(__self__, "full_snapshot_interval_slots", full_snapshot_interval_slots)
        pulumi.set(__self__, "gossip_port", gossip_port)
        pulumi.set(__self__, "limit_ledger_size", limit_ledger_size)
        pulumi.set(__self__, "no_wait_for_vote_to_start_leader", no_wait_for_vote_to_start_leader)
        pulumi.set(__self__, "only_known_rpc", only_known_rpc)
        pulumi.set(__self__, "paths", paths)
        pulumi.set(__self__, "private_rpc", private_rpc)
        pulumi.set(__self__, "rpc_bind_address", rpc_bind_address)
        pulumi.set(__self__, "rpc_port", rpc_port)
        pulumi.set(__self__, "use_snapshot_archives_at_startup", use_snapshot_archives_at_startup)
        pulumi.set(__self__, "wal_recovery_mode", wal_recovery_mode)
        if entry_point is not None:
            pulumi.set(__self__, "entry_point", entry_point)
        if expected_genesis_hash is not None:
            pulumi.set(__self__, "expected_genesis_hash", expected_genesis_hash)
        if full_rpc_api is not None:
            pulumi.set(__self__, "full_rpc_api", full_rpc_api)
        if known_validator is not None:
            pulumi.set(__self__, "known_validator", known_validator)
        if no_voting is not None:
            pulumi.set(__self__, "no_voting", no_voting)
        if tvu_receive_threads is not None:
            pulumi.set(__self__, "tvu_receive_threads", tvu_receive_threads)

    @property
    @pulumi.getter(name="blockProductionMethod")
    def block_production_method(self) -> pulumi.Input[str]:
        return pulumi.get(self, "block_production_method")

    @block_production_method.setter
    def block_production_method(self, value: pulumi.Input[str]):
        pulumi.set(self, "block_production_method", value)

    @property
    @pulumi.getter(name="dynamicPortRange")
    def dynamic_port_range(self) -> pulumi.Input[str]:
        return pulumi.get(self, "dynamic_port_range")

    @dynamic_port_range.setter
    def dynamic_port_range(self, value: pulumi.Input[str]):
        pulumi.set(self, "dynamic_port_range", value)

    @property
    @pulumi.getter(name="fullSnapshotIntervalSlots")
    def full_snapshot_interval_slots(self) -> pulumi.Input[int]:
        return pulumi.get(self, "full_snapshot_interval_slots")

    @full_snapshot_interval_slots.setter
    def full_snapshot_interval_slots(self, value: pulumi.Input[int]):
        pulumi.set(self, "full_snapshot_interval_slots", value)

    @property
    @pulumi.getter(name="gossipPort")
    def gossip_port(self) -> pulumi.Input[int]:
        return pulumi.get(self, "gossip_port")

    @gossip_port.setter
    def gossip_port(self, value: pulumi.Input[int]):
        pulumi.set(self, "gossip_port", value)

    @property
    @pulumi.getter(name="limitLedgerSize")
    def limit_ledger_size(self) -> pulumi.Input[int]:
        return pulumi.get(self, "limit_ledger_size")

    @limit_ledger_size.setter
    def limit_ledger_size(self, value: pulumi.Input[int]):
        pulumi.set(self, "limit_ledger_size", value)

    @property
    @pulumi.getter(name="noWaitForVoteToStartLeader")
    def no_wait_for_vote_to_start_leader(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "no_wait_for_vote_to_start_leader")

    @no_wait_for_vote_to_start_leader.setter
    def no_wait_for_vote_to_start_leader(self, value: pulumi.Input[bool]):
        pulumi.set(self, "no_wait_for_vote_to_start_leader", value)

    @property
    @pulumi.getter(name="onlyKnownRPC")
    def only_known_rpc(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "only_known_rpc")

    @only_known_rpc.setter
    def only_known_rpc(self, value: pulumi.Input[bool]):
        pulumi.set(self, "only_known_rpc", value)

    @property
    @pulumi.getter
    def paths(self) -> pulumi.Input['ValidatorPathsArgs']:
        return pulumi.get(self, "paths")

    @paths.setter
    def paths(self, value: pulumi.Input['ValidatorPathsArgs']):
        pulumi.set(self, "paths", value)

    @property
    @pulumi.getter(name="privateRPC")
    def private_rpc(self) -> pulumi.Input[bool]:
        return pulumi.get(self, "private_rpc")

    @private_rpc.setter
    def private_rpc(self, value: pulumi.Input[bool]):
        pulumi.set(self, "private_rpc", value)

    @property
    @pulumi.getter(name="rpcBindAddress")
    def rpc_bind_address(self) -> pulumi.Input[str]:
        return pulumi.get(self, "rpc_bind_address")

    @rpc_bind_address.setter
    def rpc_bind_address(self, value: pulumi.Input[str]):
        pulumi.set(self, "rpc_bind_address", value)

    @property
    @pulumi.getter(name="rpcPort")
    def rpc_port(self) -> pulumi.Input[int]:
        return pulumi.get(self, "rpc_port")

    @rpc_port.setter
    def rpc_port(self, value: pulumi.Input[int]):
        pulumi.set(self, "rpc_port", value)

    @property
    @pulumi.getter(name="useSnapshotArchivesAtStartup")
    def use_snapshot_archives_at_startup(self) -> pulumi.Input[str]:
        return pulumi.get(self, "use_snapshot_archives_at_startup")

    @use_snapshot_archives_at_startup.setter
    def use_snapshot_archives_at_startup(self, value: pulumi.Input[str]):
        pulumi.set(self, "use_snapshot_archives_at_startup", value)

    @property
    @pulumi.getter(name="walRecoveryMode")
    def wal_recovery_mode(self) -> pulumi.Input[str]:
        return pulumi.get(self, "wal_recovery_mode")

    @wal_recovery_mode.setter
    def wal_recovery_mode(self, value: pulumi.Input[str]):
        pulumi.set(self, "wal_recovery_mode", value)

    @property
    @pulumi.getter(name="entryPoint")
    def entry_point(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "entry_point")

    @entry_point.setter
    def entry_point(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "entry_point", value)

    @property
    @pulumi.getter(name="expectedGenesisHash")
    def expected_genesis_hash(self) -> Optional[pulumi.Input[str]]:
        return pulumi.get(self, "expected_genesis_hash")

    @expected_genesis_hash.setter
    def expected_genesis_hash(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expected_genesis_hash", value)

    @property
    @pulumi.getter(name="fullRpcAPI")
    def full_rpc_api(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "full_rpc_api")

    @full_rpc_api.setter
    def full_rpc_api(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "full_rpc_api", value)

    @property
    @pulumi.getter(name="knownValidator")
    def known_validator(self) -> Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]:
        return pulumi.get(self, "known_validator")

    @known_validator.setter
    def known_validator(self, value: Optional[pulumi.Input[Sequence[pulumi.Input[str]]]]):
        pulumi.set(self, "known_validator", value)

    @property
    @pulumi.getter(name="noVoting")
    def no_voting(self) -> Optional[pulumi.Input[bool]]:
        return pulumi.get(self, "no_voting")

    @no_voting.setter
    def no_voting(self, value: Optional[pulumi.Input[bool]]):
        pulumi.set(self, "no_voting", value)

    @property
    @pulumi.getter(name="tvuReceiveThreads")
    def tvu_receive_threads(self) -> Optional[pulumi.Input[int]]:
        return pulumi.get(self, "tvu_receive_threads")

    @tvu_receive_threads.setter
    def tvu_receive_threads(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "tvu_receive_threads", value)


@pulumi.input_type
class ValidatorKeyPairsArgs:
    def __init__(__self__, *,
                 identity: pulumi.Input[str],
                 vote_account: pulumi.Input[str]):
        pulumi.set(__self__, "identity", identity)
        pulumi.set(__self__, "vote_account", vote_account)

    @property
    @pulumi.getter
    def identity(self) -> pulumi.Input[str]:
        return pulumi.get(self, "identity")

    @identity.setter
    def identity(self, value: pulumi.Input[str]):
        pulumi.set(self, "identity", value)

    @property
    @pulumi.getter(name="voteAccount")
    def vote_account(self) -> pulumi.Input[str]:
        return pulumi.get(self, "vote_account")

    @vote_account.setter
    def vote_account(self, value: pulumi.Input[str]):
        pulumi.set(self, "vote_account", value)


@pulumi.input_type
class ValidatorPathsArgs:
    def __init__(__self__, *,
                 accounts: pulumi.Input[str],
                 ledger: pulumi.Input[str],
                 log: pulumi.Input[str]):
        pulumi.set(__self__, "accounts", accounts)
        pulumi.set(__self__, "ledger", ledger)
        pulumi.set(__self__, "log", log)

    @property
    @pulumi.getter
    def accounts(self) -> pulumi.Input[str]:
        return pulumi.get(self, "accounts")

    @accounts.setter
    def accounts(self, value: pulumi.Input[str]):
        pulumi.set(self, "accounts", value)

    @property
    @pulumi.getter
    def ledger(self) -> pulumi.Input[str]:
        return pulumi.get(self, "ledger")

    @ledger.setter
    def ledger(self, value: pulumi.Input[str]):
        pulumi.set(self, "ledger", value)

    @property
    @pulumi.getter
    def log(self) -> pulumi.Input[str]:
        return pulumi.get(self, "log")

    @log.setter
    def log(self, value: pulumi.Input[str]):
        pulumi.set(self, "log", value)


