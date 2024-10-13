from grpc import insecure_channel, Channel
from xcapi.xray.app.stats.command.command_grpc_pb import StatsServiceStub
import xcapi.xray.app.stats.command.command_pb as StatsCommand
if __name__ == '__main__':
    host: str = '127.0.0.1'
    port: str = '11514'
    channel: Channel = insecure_channel(f'{host}:{port}')
    # status
    statsServiceStub: StatsServiceStub = StatsServiceStub(channel)
    status: StatsCommand.SysStatsResponse = statsServiceStub.GetSysStats(StatsCommand.SysStatsRequest())














