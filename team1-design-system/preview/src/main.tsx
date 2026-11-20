import * as React from "react"
import { createRoot } from "react-dom/client"
import { ArrowUpRight, CalendarDays, CheckCircle2, Info, MapPin, Plus, Trophy, TriangleAlert, XCircle } from "lucide-react"
import "./preview.css"
import onDark from "../../assets/identity/wordmark/Team1_MAIN_WHITE.svg"
import onLight from "../../assets/identity/wordmark/Team1_BLACK_MAIN.svg"
import tokens from "../../tokens/design-tokens.json"
import {
  Alert, AlertDescription, AlertTitle, Badge, Button, Card, CardContent, CardDescription, CardFooter, CardHeader, CardMedia, CardTitle,
  Checkbox, Dialog, DialogClose, DialogContent, DialogDescription, DialogFooter, DialogHeader, DialogTitle, DialogTrigger,
  Input, Label, Select, SelectContent, SelectItem, SelectTrigger, SelectValue, SiteFooter, SiteHeader, Switch,
  Table, TableBody, TableCell, TableHead, TableHeader, TableRow, Tabs, TabsContent, TabsList, TabsTrigger, Textarea, ThemeToggle,
  Tooltip, TooltipContent, TooltipProvider, TooltipTrigger,
} from "@/components"

const logo = { onDarkSrc: onDark, onLightSrc: onLight, label: "Design System" }
const theme = document.documentElement.getAttribute("data-theme") ?? "dark (default)"

function Section({ id, title, kicker, children }: { id: string; title: string; kicker: string; children: React.ReactNode }) {
  return (
    <section id={id} className="container-page border-t border-line py-14">
      <p className="meta mb-2 uppercase">{kicker}</p>
      <h2 className="mb-8 text-3xl">{title}</h2>
      {children}
    </section>
  )
}

function Sub({ children }: { children: React.ReactNode }) {
  return <h3 className="mt-10 mb-4 font-sans text-sm font-medium tracking-[0.04em] text-fg-muted uppercase first:mt-0">{children}</h3>
}

function Swatch({ name, varName }: { name: string; varName: string }) {
  const ref = React.useRef<HTMLDivElement>(null)
  const [value, setValue] = React.useState("")
  React.useEffect(() => {
    if (ref.current) setValue(getComputedStyle(ref.current).getPropertyValue(varName).trim())
  }, [varName])
  return (
    <div ref={ref} className="overflow-hidden rounded-sm border border-line">
      <div className="h-14 border-b border-line" style={{ background: `var(${varName})` }} />
      <div className="px-3 py-2">
        <p className="text-xs font-medium text-fg-heading">{name}</p>
        <p className="meta truncate">{varName}</p>
        <p className="meta truncate">{value}</p>
      </div>
    </div>
  )
}

const roleVars = Object.keys(tokens.web.theme.dark)
  .filter((k) => !k.startsWith("$") && !k.startsWith("shadow"))
  .map((k) => ({ name: k, varName: `--team1-${k.replace(/([A-Z])/g, "-$1").toLowerCase()}` }))

const states = [
  { label: "Default", props: {} },
  { label: "Hover", props: { "data-preview-state": "hover" } },
  { label: "Pressed", props: { "data-preview-state": "hover active" } },
  { label: "Focus", props: { "data-preview-state": "focus" } },
  { label: "Disabled", props: { disabled: true } },
  { label: "Loading", props: { loading: true } },
] as const

const variants = ["primary", "secondary", "ghost", "destructive", "link"] as const

function App() {
  return (
    <TooltipProvider>
      <SiteHeader
        logo={logo}
        links={[
          { label: "Tokens", href: "#tokens", active: true },
          { label: "Buttons", href: "#buttons" },
          { label: "Forms", href: "#forms" },
          { label: "Cards", href: "#cards" },
          { label: "Data", href: "#data" },
        ]}
        actions={
          <>
            <ThemeToggle />
            <Button variant="ghost" size="sm" className="hidden sm:inline-flex">Sign in</Button>
            <Button size="sm">Join</Button>
          </>
        }
      />
      <main>
        <div className="container-page py-16">
          <p className="meta mb-3">TEAM1 DESIGN SYSTEM · 3.0.0 · THEME: {theme.toUpperCase()}</p>
          <h1 className="max-w-3xl text-[clamp(2.5rem,5vw,4rem)] leading-[1.02] tracking-[-0.03em]">
            Where Avalanche builders learn, hack and <span className="text-brand">ship.</span>
          </h1>
          <p className="mt-5 max-w-2xl text-lg">
            Kanit Medium headings, Inter Light for long-form reading and Inter Regular for interface text. Red is the only accent; pills for actions, 12px fields, 20px cards.
          </p>
          <div className="mt-8 flex flex-wrap gap-3">
            <Button size="lg">Join the Ecosystem Hub <ArrowUpRight /></Button>
            <Button size="lg" variant="secondary">What is Team1?</Button>
          </div>
        </div>

        <Section id="tokens" kicker="Foundations" title="Tokens">
          <Sub>Theme roles</Sub>
          <div className="grid grid-cols-2 gap-3 sm:grid-cols-4 lg:grid-cols-6">
            {roleVars.map((r) => <Swatch key={r.name} {...r} />)}
          </div>
          <Sub>Brand red scale (Ava Red = 500)</Sub>
          <div className="grid grid-cols-4 gap-3 sm:grid-cols-6 lg:grid-cols-11">
            {Object.keys(tokens.global.color.brand.scale).filter((k) => !k.startsWith("$")).map((k) => <Swatch key={k} name={`red ${k}`} varName={`--team1-red-${k}`} />)}
          </div>
          <Sub>Status (pair with icon + text, never colour alone)</Sub>
          <div className="grid grid-cols-3 gap-3 sm:grid-cols-6">
            <Swatch name="success" varName="--team1-success" />
            <Swatch name="warning" varName="--team1-warning" />
            <Swatch name="error" varName="--team1-error" />
            <Swatch name="text success" varName="--team1-text-success" />
            <Swatch name="text warning" varName="--team1-text-warning" />
            <Swatch name="text error" varName="--team1-text-error" />
          </div>
          <Sub>Typography</Sub>
          <div className="grid gap-8 lg:grid-cols-2">
            <div className="space-y-3">
              <h1 className="text-4xl">H1 Kanit Medium 36</h1>
              <h2 className="text-3xl">H2 Kanit Medium 30</h2>
              <h3 className="text-2xl">H3 Kanit Medium 24</h3>
              <h4 className="text-xl">H4 Kanit Medium 20</h4>
              <h5 className="text-lg">H5 Kanit Medium 18</h5>
              <h6 className="text-base">H6 Kanit Medium 16</h6>
            </div>
            <div className="space-y-4">
              <p className="text-lg">Body large · Inter 300 / 18 / 1.6. One builder profile for every hackathon, bounty and course you join.</p>
              <p>Body · Inter 300 / 16 / 1.6. Long-form reading text keeps the light weight from the brand book.</p>
              <p className="text-sm leading-[1.45] font-normal">UI · Inter 400 / 14. Labels, inputs, tables, navigation and captions use Regular for legibility.</p>
              <p className="text-xs leading-[1.45] font-normal text-fg-muted">Caption · Inter 400 / 12 · muted</p>
              <p className="meta">META · JETBRAINS MONO 12 · 20 NOV 2026 · #0042</p>
              <p className="text-sm">Link inside text: <a className="text-fg-brand underline underline-offset-4" href="#tokens">grant guidelines</a></p>
            </div>
          </div>
          <Sub>Radius: xs 6 · sm 12 · lg 20 · full</Sub>
          <div className="flex flex-wrap items-end gap-6">
            {[["xs", "rounded-xs", "checkbox, code, menu items"], ["sm", "rounded-sm", "fields, menus, alerts, media"], ["lg", "rounded-lg", "cards, dialogs"], ["full", "rounded-full", "buttons, badges, tabs, switch"]].map(([n, c, u]) => (
              <div key={n} className="w-44">
                <div className={`h-20 border border-line-strong bg-surface-raised ${c}`} />
                <p className="mt-2 text-sm font-medium text-fg-heading">{n}</p>
                <p className="text-xs font-normal text-fg-muted">{u}</p>
              </div>
            ))}
          </div>
          <Sub>Spacing (4px base)</Sub>
          <div className="space-y-1.5">
            {Object.entries(tokens.global.spacing).filter(([k]) => !k.startsWith("$")).sort((a, b) => parseFloat(a[0]) - parseFloat(b[0])).map(([k, v]) => (
              <div key={k} className="flex items-center gap-3">
                <span className="meta w-16">{k}</span>
                <span className="h-2 rounded-full bg-brand" style={{ width: (v as { $value: string }).$value }} />
                <span className="meta">{(v as { $value: string }).$value}</span>
              </div>
            ))}
          </div>
          <Sub>Elevation, focus and motion</Sub>
          <div className="grid gap-6 sm:grid-cols-2 lg:grid-cols-5">
            {[["shadow-card", "card (rest)"], ["shadow-card-hover", "card hover"], ["shadow-button-hover", "button hover"], ["shadow-overlay", "overlay"]].map(([c, n]) => (
              <div key={c} className={`flex h-24 items-end rounded-lg border border-line bg-surface p-4 ${c}`}><span className="text-xs font-normal text-fg-muted">{n}</span></div>
            ))}
            <div className="flex h-24 items-end rounded-lg border border-line bg-surface p-4 outline-2 outline-offset-2 outline-focus-ring"><span className="text-xs font-normal text-fg-muted">focus ring 2px + 2px offset</span></div>
          </div>
          <p className="mt-4 text-sm font-normal text-fg-muted">Motion: 150 / 200 / 300 ms, entrance 400 ms cubic-bezier(0.16, 1, 0.3, 1) with 20 px fade-up. Under prefers-reduced-motion, scale and lift are replaced by colour steps.</p>
        </Section>

        <Section id="buttons" kicker="Actions" title="Buttons">
          <div className="overflow-x-auto">
            <table className="w-full border-separate border-spacing-x-3 border-spacing-y-4 text-left">
              <thead>
                <tr>
                  <th className="meta font-normal">variant</th>
                  {states.map((s) => <th key={s.label} className="meta font-normal">{s.label}</th>)}
                </tr>
              </thead>
              <tbody>
                {variants.map((v) => (
                  <tr key={v}>
                    <td className="meta">{v}</td>
                    {states.map((s) => (
                      <td key={s.label} data-specimen={`button-${v}-${s.label.toLowerCase()}`} className="py-1">
                        <Button variant={v} {...s.props}>{v === "destructive" ? "Delete" : "Join team1"}</Button>
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <Sub>Sizes and icons</Sub>
          <div className="flex flex-wrap items-center gap-3">
            <Button size="sm">Small 36</Button>
            <Button>Default 44</Button>
            <Button size="lg">Large 52</Button>
            <Button><Plus /> With icon</Button>
            <Button size="icon" aria-label="Add"><Plus /></Button>
            <Button size="icon-sm" variant="secondary" aria-label="Add"><Plus /></Button>
          </div>
        </Section>

        <Section id="forms" kicker="Inputs" title="Forms">
          <div className="grid gap-x-8 gap-y-6 md:grid-cols-2 lg:grid-cols-3">
            <div className="grid gap-2"><Label htmlFor="f1">Project name</Label><Input id="f1" placeholder="e.g. Subnet Explorer" /></div>
            <div className="grid gap-2"><Label htmlFor="f2">Filled</Label><Input id="f2" defaultValue="Fuji Pulse" /></div>
            <div className="grid gap-2"><Label htmlFor="f3">Hover</Label><Input id="f3" defaultValue="Hovered field" data-preview-state="hover" /></div>
            <div className="grid gap-2"><Label htmlFor="f4">Focus</Label><Input id="f4" defaultValue="Focused field" data-preview-state="focus" /></div>
            <div className="grid gap-2">
              <Label htmlFor="f5">Invalid</Label>
              <Input id="f5" defaultValue="not-an-email" aria-invalid aria-describedby="f5e" />
              <p id="f5e" className="flex items-center gap-1.5 text-xs font-normal text-fg-error"><XCircle className="size-3.5" aria-hidden /> Enter a valid email address.</p>
            </div>
            <div className="grid gap-2"><Label htmlFor="f6">Disabled</Label><Input id="f6" defaultValue="Locked" disabled /></div>
            <div className="grid gap-2 md:col-span-2"><Label htmlFor="f7">Description</Label><Textarea id="f7" placeholder="What are you building?" /></div>
            <div className="grid gap-2">
              <Label>Track</Label>
              <Select defaultValue="infra">
                <SelectTrigger aria-label="Track"><SelectValue /></SelectTrigger>
                <SelectContent>
                  <SelectItem value="infra">Infrastructure</SelectItem>
                  <SelectItem value="defi">DeFi</SelectItem>
                  <SelectItem value="gaming">Gaming</SelectItem>
                </SelectContent>
              </Select>
              <Select>
                <SelectTrigger aria-label="Track placeholder" data-preview-state="focus"><SelectValue placeholder="Choose a track (focus)" /></SelectTrigger>
                <SelectContent><SelectItem value="a">A</SelectItem></SelectContent>
              </Select>
            </div>
          </div>
          <Sub>Checkbox and switch</Sub>
          <div className="flex flex-wrap items-center gap-8">
            <Label className="font-normal"><Checkbox /> Unchecked</Label>
            <Label className="font-normal"><Checkbox defaultChecked /> Checked</Label>
            <Label className="font-normal"><Checkbox data-preview-state="focus" /> Focus</Label>
            <Label className="font-normal"><Checkbox disabled defaultChecked /> Disabled</Label>
            <Label className="font-normal"><Switch /> Off</Label>
            <Label className="font-normal"><Switch defaultChecked /> On</Label>
            <Label className="font-normal"><Switch defaultChecked data-preview-state="focus" /> Focus</Label>
            <Label className="font-normal"><Switch disabled /> Disabled</Label>
          </div>
        </Section>

        <Section id="cards" kicker="Surfaces" title="Cards, badges, tabs">
          <Sub>Badges</Sub>
          <div className="flex flex-wrap gap-2">
            {(["brand", "solid", "neutral", "outline", "success", "warning", "error"] as const).map((v) => <Badge key={v} variant={v}>{v}</Badge>)}
          </div>
          <Sub>Glow card (default) · rest and hover</Sub>
          <div className="grid gap-6 md:grid-cols-3" data-specimen="cards-glow">
            {[{ s: undefined, t: "Team1 UniHack" }, { s: "hover", t: "Social Night (hover)" }].map(({ s, t }) => (
              <Card key={t} interactive data-preview-state={s}>
                <CardMedia className="mt-0 h-32 bg-[radial-gradient(ellipse_at_top_right,rgb(230_33_47/0.45),transparent_60%)] bg-surface-raised" />
                <CardHeader>
                  <div className="flex gap-2"><Badge variant="brand">Hackathon</Badge><Badge>Online</Badge></div>
                  <CardTitle>{t}</CardTitle>
                  <CardDescription className="flex items-center gap-3"><span className="inline-flex items-center gap-1"><CalendarDays className="size-3.5" /> 20 Nov</span><span className="inline-flex items-center gap-1"><MapPin className="size-3.5" /> Istanbul</span></CardDescription>
                </CardHeader>
                <CardFooter><Button size="sm">Register</Button><Button size="sm" variant="ghost">Details</Button></CardFooter>
              </Card>
            ))}
            <Card>
              <CardHeader><CardTitle>Static glow card</CardTitle><CardDescription>Non-interactive content block</CardDescription></CardHeader>
              <CardContent><p className="text-sm font-normal">Glow is the default card treatment. Use one glow level per surface; nested cards are quiet.</p></CardContent>
            </Card>
          </div>
          <Sub>Quiet card (dense lists)</Sub>
          <div className="grid gap-3 md:grid-cols-2" data-specimen="cards-quiet">
            {["Subnet Explorer", "Fuji Pulse (hover)", "AvaPay", "Validator Watch"].map((n, i) => (
              <Card key={n} variant="quiet" interactive className="flex-row items-center gap-4 px-5 py-4" data-preview-state={i === 1 ? "hover" : undefined}>
                <Trophy className="size-5 text-fg-brand" aria-hidden />
                <div className="flex-1"><p className="text-sm font-medium text-fg-heading">{n}</p><p className="meta">BUILT DURING UNIHACK · #{i + 12}</p></div>
                <ArrowUpRight className="size-4 text-fg-muted" aria-hidden />
              </Card>
            ))}
          </div>
          <Sub>Tabs and tooltip</Sub>
          <div className="flex flex-wrap items-start gap-10">
            <Tabs defaultValue="overview">
              <TabsList>
                <TabsTrigger value="overview">Overview</TabsTrigger>
                <TabsTrigger value="tracks">Tracks</TabsTrigger>
                <TabsTrigger value="prizes" data-preview-state="focus">Prizes (focus)</TabsTrigger>
                <TabsTrigger value="faq" disabled>FAQ</TabsTrigger>
              </TabsList>
              <TabsContent value="overview"><p className="text-sm font-normal">Three days, four tracks, one builder profile.</p></TabsContent>
            </Tabs>
            <div className="pt-1 pb-12">
              <Tooltip open>
                <TooltipTrigger asChild><Button variant="secondary" size="sm"><Info /> Hover for info</Button></TooltipTrigger>
                <TooltipContent side="bottom">Submissions close Friday 18:00 CET</TooltipContent>
              </Tooltip>
            </div>
            <Dialog>
              <DialogTrigger asChild><Button variant="secondary" size="sm" data-specimen="dialog-trigger">Open dialog</Button></DialogTrigger>
              <DialogContent>
                <DialogHeader>
                  <DialogTitle>Submit your project?</DialogTitle>
                  <DialogDescription>You can edit the submission until the deadline. Judges see the version submitted at 18:00 CET.</DialogDescription>
                </DialogHeader>
                <div className="grid gap-2"><Label htmlFor="d1">Demo URL</Label><Input id="d1" placeholder="https://" /></div>
                <DialogFooter>
                  <DialogClose asChild><Button variant="ghost">Cancel</Button></DialogClose>
                  <Button>Submit project</Button>
                </DialogFooter>
              </DialogContent>
            </Dialog>
          </div>
        </Section>

        <Section id="data" kicker="Data and feedback" title="Table and alerts">
          <Table>
            <TableHeader><TableRow><TableHead>Project</TableHead><TableHead>Track</TableHead><TableHead>Status</TableHead><TableHead className="text-right">Prize</TableHead></TableRow></TableHeader>
            <TableBody>
              <TableRow><TableCell className="font-medium text-fg-heading">Subnet Explorer</TableCell><TableCell>Infra</TableCell><TableCell><Badge variant="success">Submitted</Badge></TableCell><TableCell className="text-right">$5,000</TableCell></TableRow>
              <TableRow data-state="selected"><TableCell className="font-medium text-fg-heading">Fuji Pulse (selected)</TableCell><TableCell>Data</TableCell><TableCell><Badge variant="warning">In review</Badge></TableCell><TableCell className="text-right">$2,500</TableCell></TableRow>
              <TableRow><TableCell className="font-medium text-fg-heading">AvaPay</TableCell><TableCell>Payments</TableCell><TableCell><Badge variant="solid">Winner</Badge></TableCell><TableCell className="text-right">$10,000</TableCell></TableRow>
            </TableBody>
          </Table>
          <div className="mt-8 grid gap-3 md:grid-cols-2">
            <Alert><Info aria-hidden /><AlertTitle>Info (neutral)</AlertTitle><AlertDescription>Office hours move to Thursday this week.</AlertDescription></Alert>
            <Alert variant="success"><CheckCircle2 aria-hidden /><AlertTitle>Registered</AlertTitle><AlertDescription>We sent the details to your email.</AlertDescription></Alert>
            <Alert variant="warning"><TriangleAlert aria-hidden /><AlertTitle>Deadline in 2 hours</AlertTitle><AlertDescription>Save your draft before 18:00 CET.</AlertDescription></Alert>
            <Alert variant="error"><XCircle aria-hidden /><AlertTitle>Submission failed</AlertTitle><AlertDescription>The demo URL is not reachable. Check it and try again.</AlertDescription></Alert>
          </div>
        </Section>
      </main>
      <SiteFooter
        logo={{ onDarkSrc: onDark, onLightSrc: onLight }}
        columns={[
          { title: "Ecosystem Hub", links: [{ label: "Events", href: "#" }, { label: "Projects", href: "#" }, { label: "Education", href: "#" }] },
          { title: "Team1", links: [{ label: "team1.network", href: "https://team1.network", external: true }, { label: "Cascade", href: "https://cascade.team1.network", external: true }] },
          { title: "Build", links: [{ label: "GitHub", href: "https://github.com/avalancheteam1", external: true }, { label: "Workshops", href: "https://github.com/avalancheteam1/workshops", external: true }] },
        ]}
        legal="© 2026 Team1 · Design System 3.0.0 preview"
      />
    </TooltipProvider>
  )
}

createRoot(document.getElementById("root")!).render(<App />)
