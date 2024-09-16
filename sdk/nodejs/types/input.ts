// *** WARNING: this file was generated by pulumi-language-nodejs. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";

import * as utilities from "../utilities";

export namespace agave {
    export interface FlagsArgs {
        blockProductionMethod: pulumi.Input<string>;
        dynamicPortRange: pulumi.Input<string>;
        entryPoint?: pulumi.Input<pulumi.Input<string>[]>;
        expectedGenesisHash?: pulumi.Input<string>;
        fullRpcAPI?: pulumi.Input<boolean>;
        fullSnapshotIntervalSlots: pulumi.Input<number>;
        gossipPort: pulumi.Input<number>;
        knownValidator?: pulumi.Input<pulumi.Input<string>[]>;
        limitLedgerSize: pulumi.Input<number>;
        noVoting?: pulumi.Input<boolean>;
        noWaitForVoteToStartLeader: pulumi.Input<boolean>;
        onlyKnownRPC: pulumi.Input<boolean>;
        privateRPC: pulumi.Input<boolean>;
        rpcBindAddress: pulumi.Input<string>;
        rpcPort: pulumi.Input<number>;
        tvuReceiveThreads?: pulumi.Input<number>;
        useSnapshotArchivesAtStartup: pulumi.Input<string>;
        walRecoveryMode: pulumi.Input<string>;
    }

    export interface KeyPairsArgs {
        identity: pulumi.Input<string>;
        voteAccount: pulumi.Input<string>;
    }
}

export namespace ssh {
    /**
     * Instructions for how to connect to a remote endpoint.
     */
    export interface ConnectionArgs {
        /**
         * SSH Agent socket path. Default to environment variable SSH_AUTH_SOCK if present.
         */
        agentSocketPath?: pulumi.Input<string>;
        /**
         * Max allowed errors on trying to dial the remote host. -1 set count to unlimited. Default value is 10.
         */
        dialErrorLimit?: pulumi.Input<number>;
        /**
         * The address of the resource to connect to.
         */
        host: pulumi.Input<string>;
        /**
         * The password we should use for the connection.
         */
        password?: pulumi.Input<string>;
        /**
         * Max number of seconds for each dial attempt. 0 implies no maximum. Default value is 15 seconds.
         */
        perDialTimeout?: pulumi.Input<number>;
        /**
         * The port to connect to. Defaults to 22.
         */
        port?: pulumi.Input<number>;
        /**
         * The contents of an SSH key to use for the connection. This takes preference over the password if provided.
         */
        privateKey?: pulumi.Input<string>;
        /**
         * The password to use in case the private key is encrypted.
         */
        privateKeyPassword?: pulumi.Input<string>;
        /**
         * The user that we should use for the connection.
         */
        user?: pulumi.Input<string>;
    }
    /**
     * connectionArgsProvideDefaults sets the appropriate defaults for ConnectionArgs
     */
    export function connectionArgsProvideDefaults(val: ConnectionArgs): ConnectionArgs {
        return {
            ...val,
            dialErrorLimit: (val.dialErrorLimit) ?? 10,
            perDialTimeout: (val.perDialTimeout) ?? 15,
            port: (val.port) ?? 22,
            user: (val.user) ?? "root",
        };
    }
}
